import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

# Clase para manejar la conexión a la base de datos
class Database():
    #@staticmethod
    def get_connection(self):
        try:
            conex = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME"),
                port=int(os.getenv("DB_PORT")) # Usa variable de entorno o 3306 por defecto MySQL
            )
            if conex.is_connected():
                print("Conexión a la base de datos exitosa.")
                return conex

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        



