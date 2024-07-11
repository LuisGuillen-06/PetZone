from flask import Flask, render_template, request, redirect, url_for, flash
from db import ConexionMySQL
from controllerDB import *
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.access(UPLOAD_FOLDER, os.W_OK):
    raise PermissionError(f"No write permissions for the folder {UPLOAD_FOLDER}")
if not os.access(UPLOAD_FOLDER, os.R_OK):
    raise PermissionError(f"No read permissions for the folder {UPLOAD_FOLDER}")

print("Read and write permissions are set correctly.")

app = Flask(__name__)
app.secret_key='1234'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear la carpeta 'uploads' si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/nuevo_producto')
def cargar_producto():
    return render_template('formularioProducto.html')

@app.route('/Guardar_Nuevo_Producto', methods=['POST'])
def insertar_nuevo_producto():
    _nombre = request.form['nombre']
    _descr = request.form['descripcion']
    _precio = request.form['precio']
    _foto = request.files['file']
    
    if _foto and allowed_file(_foto.filename):
        filename = secure_filename(_foto.filename)
        _foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filas_afectadas = Agregar_Nuevo_Producto(_nombre, _descr, _precio, filename)
        
        if filas_afectadas > 0:
            flash('Producto agregado exitosamente', 'success')
            return redirect(url_for('lista_productos'))
        else:
            flash('Error al agregar el producto', 'danger')
            return "Error al agregar el producto", 500
        
    else:
        flash('Error al subir la imagen del producto', 'danger')
        return redirect(url_for('cargar_producto'))

@app.route('/tienda')
def tienda():
    productos = GetProductos()
    return render_template('tienda.html', productos=productos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lista_productos')
def lista_productos():
    productos = GetProductos()
    return render_template('lista_productos.html', productos=productos)

@app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    
    producto = GetProductoPorId(id)
    
    if request.method == 'POST':
        _nombre = request.form['nombre']
        _descr = request.form['descripcion']
        _precio = request.form['precio']
        _foto = request.files['file']
        foto_anterior = request.form['foto_anterior']
        
        if _foto and allowed_file(_foto.filename):
            filename = secure_filename(_foto.filename)
            _foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            if foto_anterior:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],foto_anterior))
                except FileNotFoundError:
                    pass
                
            filas_afectadas = Editar_Producto(id, _nombre, _descr, _precio, filename)
        else:
            filas_afectadas = Editar_Producto(id, _nombre, _descr, _precio, foto_anterior)
        
        if filas_afectadas > 0:
            return redirect(url_for('lista_productos'))
        else:
            return "Error al actualizar el producto", 500
    
    return render_template('editar_producto.html', producto=producto)


@app.route('/eliminar_producto/<int:id>')
def eliminar_producto(id):
    producto = GetProductoPorId(id)
    if producto and producto[4]:  # Verifica si el producto y la imagen existen
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], producto[4]))
        except FileNotFoundError:
            pass
    Eliminar_Producto(id)
    return redirect(url_for('lista_productos'))


@app.route('/buscar_productos', methods=['GET'])
def buscar_productos():
    q = request.args.get('q', '')
    if q:
        productos = Buscar_Productos(q)
    else:
        productos = GetProductos()
    return render_template('lista_productos.html', productos=productos)


if __name__ == '__main__':
    app.run(debug=True)
