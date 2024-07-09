import pymysql

host="localhost"
user="root"
password=""
db="bd_flask"

def ConexionMySQL():
    return pymysql.connect(host=host,user=user,password=password,database=db)

