import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='buhwzhsriixdqrq8eiwy-mysql.services.clever-cloud.com',
            user='uh9qjhykmokmqdbi',
            password='SuWnSszbnfqsUtMC0mPy',
            database='buhwzhsriixdqrq8eiwy',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida con la base de datos")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
