
import mysql.connector
from domain.entities.usuario import Usuario
from domain.repositories.usuario_dao import IUsuarioDao
from core.database import Database

# Implementación concreta de IUsuarioDao para MySQL
class MySQLUsuarioDAO(IUsuarioDao):
    # Varible de clase, hace que todas las instancias compartan la misma conexión. No es lo mas adecuado.
    # conexion = Database().get_connection()
    # Sería mejor manejar la conexión en cada método o usar un patrón de diseño como Singleton

    def __init__(self):
        # Creo una instancia de la base de datos para cada DAO
        self.database = Database()

    def _get_connection(self):
        """Obtiene una nueva conexión para cada operación"""
        return self.database.get_connection()

    def agregar_usuario(self, usuario: Usuario):
        # El bloque 'with self.conexion:' no es correcto aquí.
        # El objeto de conexión de mysql.connector no implementa el protocolo de contexto (no es compatible con 'with').
        # En su lugar, se recomienda usar 'with' con el cursor:
        conexion = self._get_connection()
        if not conexion:
            print("No se pudo establecer la conexión a la base de datos.")
            return
        with conexion.cursor() as cursor:
            try:
                query = "INSERT INTO usuario (correo, nombres, apellidos, contrasena, es_activo) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (usuario.correo, usuario.nombres, usuario.apellidos, usuario.contrasena, usuario.es_activo))
                conexion.commit()
                print(f"Usuario agregado con exito: {usuario.correo}")
            except mysql.connector.Error as err:
                print(f"Error al agregar usuario: {err}")
                conexion.rollback()

    def obtener_usuario(self, correo: str) -> Usuario:
        """Obtiene un usuario por su correo"""
        conexion = self._get_connection()
        if not conexion:
            print("No se pudo establecer la conexión a la base de datos.")
            return
        with conexion.cursor() as cursor:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = "SELECT * FROM usuario WHERE correo = %s"
                cursor.execute(query, (correo,))
                result = cursor.fetchone()
                if result:
                        return Usuario(correo=result['correo'], nombre=result['nombres'], apellidos=result['apellidos'], contrasena=result['contrasena'])
                else:
                    print("Usuario no encontrado.")
                    return None 
            except mysql.connector.Error as err:
                print(f"Error al obtener usuario: {err}")
                return None
            finally:
                cursor.close()
                self.conexion.close()

    def eliminar_usuario(self, usuario_id: int):
        if self.conexion:
            try:
                cursor = self.conexion.cursor()
                query = "DELETE FROM usuario WHERE id = %s"
                cursor.execute(query, (usuario_id,))
                self.conexion.commit()
                print(f"Usuario eliminado con ID: {usuario_id}")
            except mysql.connector.Error as err:
                print(f"Error al eliminar usuario: {err}")
                self.conexion.rollback()
            finally:
                cursor.close()
                self.conexion.close()

    def listar_usuarios(self) -> list[Usuario]:
        if self.conexion:
            try:
                cursor = self.conexion.cursor(dictionary=True)
                query = "SELECT * FROM usuario"
                cursor.execute(query)
                results = cursor.fetchall()
                return [Usuario(id=row['id'], email=row['correo'], nombre=row['nombre'], apellido=row['apellido'], contraseña=row['contraseña']) for row in results]
            except mysql.connector.Error as err:
                print(f"Error al listar usuarios: {err}")
                return []
            finally:
                cursor.close()
                self.conexion.close()