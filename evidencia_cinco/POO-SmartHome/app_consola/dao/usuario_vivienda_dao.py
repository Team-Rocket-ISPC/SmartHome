
from dao.interfaces.interface_usuario_vivienda import IDataAccessUsuarioViviendaDAO
from domain.entities.usuario_vivienda import UsuarioVivienda


class UsuarioViviendaDAO(IDataAccessUsuarioViviendaDAO):
    """Implementación concreta de la interfaz IDataAccessUsuarioViviendaDAO para manejar las operaciones CRUD de UsuarioVivienda en la base de datos."""
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, usuario_vivienda : UsuarioVivienda) -> bool:
        """Crea un nuevo registro de UsuarioVivienda en la base de datos."""
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO usuario_vivienda (usuario_id, vivienda_id) VALUES (%s, %s)"
            values = (usuario_vivienda.usuario_id, usuario_vivienda.vivienda_id)
            cursor.execute(query, values)
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error al crear UsuarioVivienda: {e}")
            return False

    def get(self, correo: str) -> UsuarioVivienda:
        """Obtiene un registro de UsuarioVivienda por su correo."""
        try:
            cursor = self.db_connection.cursor()
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
            cursor = self.db_connection.cursor()
            query = "UPDATE usuario_vivienda SET usuario_id = %s, vivienda_id = %s WHERE correo = %s"
            values = (usuario_vivienda.usuario_id, usuario_vivienda.vivienda_id, correo)
            cursor.execute(query, values)
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar UsuarioVivienda: {e}")
            return False

    def delete(self, correo: str) -> bool:
        """Elimina un registro de UsuarioVivienda de la base de datos."""
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM usuario_vivienda WHERE correo = %s"
            cursor.execute(query, (correo,))
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar UsuarioVivienda: {e}")
            return False