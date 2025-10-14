from dao.interfaces.interface_tipo_dispositivo_dao import IDataAccessTipoDispositivoDAO
from domain.entities.tipo_dispositivo import TipoDispositivo
from conn.db_conn import DBConn

class DataAccessTipoDispositivoDAO(IDataAccessTipoDispositivoDAO):
    """Implementación de la interfaz de acceso a datos para TipoDispositivo usando MySQL."""
    def get(self, id_tipo: int) -> TipoDispositivo:
        """Retorna un tipo de dispositivo por su ID."""
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_tipo, nombre FROM tipo_dispositivo WHERE id_tipo=%s"
                cursor.execute(query, (id_tipo,))
                row = cursor.fetchone()
                if row:
                    return TipoDispositivo(row[1], row[0])
                return None
            except Exception as e:
                print(f"[DAO] Error al obtener Tipo de dispositivo: {e}")
                return None

    def get_all(self) -> list[TipoDispositivo]:
        """Retorna una lista con todos los tipos de dispositivo en la base de datos."""
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_tipo, nombre FROM tipo_dispositivo"
                cursor.execute(query)
                rows = cursor.fetchall()
                tipos = [TipoDispositivo(row[1], row[0]) for row in rows]
                return tipos
            except Exception as e:
                print(f"[DAO] Error al obtener Tipos de dispositivo: {e}")
                return None    

    def create(self, tipo_dispositivo: TipoDispositivo) -> bool:
        """Inserta un nuevo tipo de dispositivo en la base de datos."""
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO tipo_dispositivo (nombre) VALUES (%s)"#no le paso id porque la BD lo autoincrementa
                cursor.execute(query, (tipo_dispositivo.nombre,))
                tipo_dispositivo.id_tipo = cursor.lastrowid  #actualiza el objeto cuyo id era none
                conn.commit()
                return tipo_dispositivo
            except Exception as e:
                print(f"[DAO] Error al crear Tipo de dispositivo: {e}")
                return False
    
    def update(self, tipo_dispositivo: TipoDispositivo) -> bool:
        """Actualiza un tipo de dispositivo existente en la base de datos."""
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE tipo_dispositivo SET nombre=%s WHERE id_tipo=%s"
                cursor.execute(query, (tipo_dispositivo.nombre, tipo_dispositivo.id_tipo))
                conn.commit()
                return  cursor.rowcount > 0  # True si se actualizó al menos un registro
            except Exception as e:
                print(f"[DAO] Error al actualizar Tipo de dispositivo: {e}")
                return False

    def delete(self, id_tipo: int) -> bool:
        """Elimina un tipo de dispositivo de la base de datos."""
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM tipo_dispositivo WHERE id_tipo=%s"
                cursor.execute(query, (id_tipo,))
                conn.commit()
                return  cursor.rowcount > 0  # True si se eliminó al menos un registro
            except Exception as e:
                print(f"[DAO] Error al eliminar Tipo de dispositivo: {e}")
                return False

    def __connect_to_mysql(self):
        """Conectar a una base de datos MySQL Server"""
        db = DBConn()
        connection = db.connect()  
        return connection
    
