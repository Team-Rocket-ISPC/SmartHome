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
        self.auth_plugin = os.getenv("AUTH_PLUGIN")  # 'mysql_native_password'
        self.use_pure = os.getenv("USE_PURE")  # 'True' o 'False'

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                auth_plugin=self.auth_plugin,
                use_pure=self.use_pure
            )
            return conn
        except mysql.connector.Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            return None


