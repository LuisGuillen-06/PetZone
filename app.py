from flask import Flask
from flask import render_template, request,redirect
from db import ConexionMySQL
from controllerDB import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('inicio.html')


@app.route('/nuevo_producto')
def Cargar_Producto():
    return render_template('formularioProducto.html')

@app.route('/Guardar_Nuevo_Producto',methods=['POST'])
def Insertar_Nuevo_Producto():
    
    _nombre = request.form['nombre']
    _descr = request.form['descripcion']
    _precio = request.form['precio']
    _foto = request.files['file']
    
    Agregar_Nuevo_Producto(_nombre,_descr,_precio,_foto)
    
    return redirect("/tienda")

@app.route('/tienda')
def Tienda():
    Productos = GetProductos()
    return render_template('/tienda.html',productos= Productos)
    

@app.route('/contacto')
def Contacto():
    return render_template("/contacto.html")

if __name__== '__main__':
    app.run(debug=True)