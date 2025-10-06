import mysql.connector
from mysql.connector import errorcode
from dao.interfaces.interface_tipo_dispositivo_dao import IDataAccessTipoDispositivoDAO
from domain.entities.tipo_dispositivo import TipoDispositivo
from conn.db_conn import DBConn

class DataAccessTipoDispositivoDAO(IDataAccessTipoDispositivoDAO):

    def get(self, id_tipo: int) -> TipoDispositivo:
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_tipo, nombre FROM tipo_dispositivo WHERE id_tipo=%s"
                cursor.execute(query, (id_tipo,))
                row = cursor.fetchone()
                if row:
                    return DataAccessTipoDispositivoDAO(row[0], row[1])
                return None
            except mysql.connector.Error as err:
                raise err
            

    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection