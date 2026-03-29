import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="crm_importaciones"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None