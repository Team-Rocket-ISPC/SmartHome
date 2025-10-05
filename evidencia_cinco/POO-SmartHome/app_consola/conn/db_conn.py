import mysql.connector
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class DBConn:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = int(os.getenv("DB_PORT"))  # valor por defecto 3306

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("✅ Conexión establecida con la base de datos")
            return conn
        except mysql.connector.Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    db = DBConn()
    connection = db.connect()
