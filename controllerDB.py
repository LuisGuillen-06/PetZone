from db import ConexionMySQL

def GetProductos():
    conexion = ConexionMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "SELECT * FROM producto;"
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        conexion.close()
    
    return result

def Agregar_Nuevo_Producto(nombre, descripcion, precio, foto):
    conexion = ConexionMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "INSERT INTO producto (nombre, descripcion, precio, foto) VALUES (%s, %s, %s, %s);"
            cursor.execute(query, (nombre, descripcion, precio, foto))
            conexion.commit()
            filas_afectadas = cursor.rowcount
    finally:
        conexion.close()
    
    return filas_afectadas

def Editar_Producto(id, nombre, descripcion, precio, foto):
    conexion = ConexionMySQL()
    filas_afectadas = 0
    try:
        with conexion.cursor() as cursor:
            if foto:
                query = "UPDATE producto SET nombre=%s, descripcion=%s, precio=%s, foto=%s WHERE id=%s;"
                cursor.execute(query, (nombre, descripcion, precio, foto, id))
            else:
                query = "UPDATE producto SET nombre=%s, descripcion=%s, precio=%s WHERE id=%s;"
                cursor.execute(query, (nombre, descripcion, precio, id))
            conexion.commit()
            filas_afectadas = cursor.rowcount
    finally:
        conexion.close()
    
    return filas_afectadas

def Eliminar_Producto(id):
    conexion = ConexionMySQL()
    filas_afectadas = 0
    try:
        with conexion.cursor() as cursor:
            query = "DELETE FROM producto WHERE id=%s;"
            cursor.execute(query, (id,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
    finally:
        conexion.close()
    
    return filas_afectadas

def GetProductoPorId(id):
    conexion = ConexionMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "SELECT * FROM producto WHERE id=%s;"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
    finally:
        conexion.close()
    
    return result

def Buscar_Productos(q):
    conexion = ConexionMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "SELECT * FROM producto WHERE nombre LIKE %s OR descripcion LIKE %s;"
            cursor.execute(query, (f'%{q}%', f'%{q}%'))
            productos = cursor.fetchall()
    finally:
        conexion.close()
    
    return productos
