from db import ConexionMySQL

def GetProductos():
    conexion = ConexionMySQL()
    
    with conexion.cursor() as cursor:
        query="SELECT * FROM producto;"
        
        cursor.execute(query)
        
        result= cursor.fetchall()
        
        conexion.commit()
        conexion.close()
        
        return result
    
def Agregar_Nuevo_Producto(nombre,descripcion,precio,foto):
    conexion = ConexionMySQL()
    
    with conexion.cursor() as cursor:
        
        query="INSERT INTO producto (nombre,descripcion,precio,foto) VALUES (%s,%s,%s,%s);"
        
        cursor.execute(query,(nombre,descripcion,precio,foto))
        result = cursor
        conexion.commit()
        conexion.close()
        
        return result