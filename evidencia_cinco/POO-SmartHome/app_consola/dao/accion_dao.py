import mysql.connector
from mysql.connector import errorcode
from dao.interfaces.interface_accion_dao import IDataAccessaccionDAO
from domain.entities.accion import Accion
from conn.db_conn import DBConn

class DataAccessAccionDAO(IDataAccessaccionDAO):

    def get(self, id_acccion: int) -> Accion:
        with self.__connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_accion, nombre, id_tipo,  FROM accion WHERE id_tipo=%s"
                cursor.execute(query, (id_acccion,))
                row = cursor.fetchone()
                if row:
                    return DataAccessAccionDAO(row[0], row[1], row[2])
                return None
            except mysql.connector.Error as err:
                raise err
            

    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection