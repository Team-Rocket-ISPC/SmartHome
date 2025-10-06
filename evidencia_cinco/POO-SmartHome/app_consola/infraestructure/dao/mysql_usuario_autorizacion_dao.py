import mysql.connector
from domain.repositories.usuario_autorizacion_dao import IUsuarioAutorizacionDao
from domain.entities.usuario_autenticacion import UsuarioAutenticacion
from core.database import Database


# Implementación concreta de IUsuarioAutorizacionDao para MySQL
class MySQLUsuarioAutorizacionDAO(IUsuarioAutorizacionDao):
    """Implementación concreta de IUsuarioAutorizacionDao para MySQL"""
    def __init__(self):
        # Creo una instancia de la base de datos para el DAO
        self.database = Database()

    def _get_connection(self):
        """Obtiene una nueva conexión para cada operación"""
        return self.database.get_connection()

    def __str__(self):
        return super().__str__()

    def autorizar_usuario(self, correo: str, contrasena: str) -> UsuarioAutenticacion:
        conexion = self._get_connection()
        if not conexion:
            print("No se pudo establecer la conexión a la base de datos.")
            return None
        with conexion.cursor() as cursor:
            try:
                query = "SELECT * FROM usuario WHERE correo = %s AND contrasena = %s"
                cursor.execute(query, (correo, contrasena))
                result = cursor.fetchone()
                # Si se encuentra el usuario, se retorna una instancia de Usuario
                if result:
                    return UsuarioAutenticacion(result[0], result[1], result[2], result[3], result[4], is_auth=True, role='Estandar')
                else:
                    print("Usuario no encontrado o contraseña incorrecta.")
                    return None
            except mysql.connector.Error as err:
                print(f"Error al autorizar usuario: {err}")
                return None
            finally:
                cursor.close()
                conexion.close()
