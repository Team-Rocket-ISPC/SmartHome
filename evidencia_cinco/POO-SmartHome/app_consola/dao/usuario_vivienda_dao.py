
from dao.interfaces.interface_usuario_vivienda import IDataAccessUsuarioViviendaDAO
from domain.entities.usuario_vivienda import UsuarioVivienda
from conn.db_conn import DBConn

class UsuarioViviendaDAO(IDataAccessUsuarioViviendaDAO):
    """Implementación concreta de la interfaz IDataAccessUsuarioViviendaDAO para manejar las operaciones CRUD de UsuarioVivienda en la base de datos."""

    def create(self, usuario_vivienda : UsuarioVivienda) -> bool:
        """Crea un nuevo registro de UsuarioVivienda en la base de datos."""
        try:
            with self.__connect_to_mysql() as conexion:
                if not conexion:
                    return False
                cursor = conexion.cursor()
                query = "INSERT INTO usuario_vivienda (usuario_id, vivienda_id) VALUES (%s, %s)"
                values = (usuario_vivienda.usuario_id, usuario_vivienda.vivienda_id)
                cursor.execute(query, values)
                conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear UsuarioVivienda: {e}")
            return False

    def get(self, correo: str) -> UsuarioVivienda:
        """Obtiene un registro de UsuarioVivienda por su correo."""
        try:
            with self.__connect_to_mysql() as conexion:
                if not conexion:
                    return None
                cursor = conexion.cursor()
                query = "SELECT * FROM usuario_vivienda WHERE correo = %s"
                cursor.execute(query, (correo,))
                result = cursor.fetchone()
                if result:
                    return UsuarioVivienda(id=result[0], usuario_id=result[1], vivienda_id=result[2])
            return None
        except Exception as e:
            print(f"Error al obtener UsuarioVivienda: {e}")
            return None

    def update(self, correo: str, usuario_vivienda: UsuarioVivienda) -> bool:
        """Actualiza un registro de UsuarioVivienda en la base de datos."""
        try:
            with self.__connect_to_mysql() as conexion:
                if not conexion:
                    return False
                cursor = conexion.cursor()
                query = "UPDATE usuario_vivienda SET usuario_id = %s, vivienda_id = %s WHERE correo = %s"
                values = (usuario_vivienda.usuario_id, usuario_vivienda.vivienda_id, correo)
                cursor.execute(query, values)
                conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar UsuarioVivienda: {e}")
            return False

    def delete(self, correo: str) -> bool:
        """Elimina un registro de UsuarioVivienda de la base de datos."""
        try:
            with self.__connect_to_mysql() as conexion:
                if not conexion:
                    return False
                cursor = conexion.cursor()
                query = "DELETE FROM usuario_vivienda WHERE correo = %s"
                cursor.execute(query, (correo,))
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al eliminar UsuarioVivienda: {e}")
            return False
        
    def cambio_rol(self, correo: str, nuevo_rol: str) -> bool:
        """Cambia el rol de un usuario dado su correo."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                print("[DAO] No se pudo conectar a la base de datos.")
                return False
            try:
                cursor = conexion.cursor()
                sql = "UPDATE usuario_vivienda SET rol = %s WHERE correo = %s"
                valores = (nuevo_rol, correo)
                res = cursor.execute(sql, valores)
                if res == 0:
                    print("[DAO] No se encontró el usuario para cambiar el rol.")
                    return False
                conexion.commit()
                return True
            except Exception as e:
                print(f"[DAO] Error al cambiar rol de usuario: {e}")
                conexion.rollback()
                return False
            
    def __connect_to_mysql(self):
        try:
            db = DBConn()
            return db.connect()
        except Exception as e:
            print(f"[DAO] Error al conectar a la base de datos: {e}")
            return None