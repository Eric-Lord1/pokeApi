import mysql.connector
import os

db_config = {
    "host": os.getenv("MYSQL_HOST", "db"),
    "user": os.getenv("MYSQL_USER", "user"),
    "password": os.getenv("MYSQL_PASSWORD", "System"),
    "database": os.getenv("MYSQL_DATABASE", "pokedb"),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

def get_db_connection():
    try:
        print("Intentando conectar a la base de datos...")
        conn = mysql.connector.connect(**db_config)
        print("Conexión exitosa.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        raise
