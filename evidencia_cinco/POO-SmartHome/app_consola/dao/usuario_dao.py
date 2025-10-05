import mysql.connector
from mysql.connector import errorcode
from dao.interfaces.interface_usuario_dao import IDataAccessUsuarioDAO
from domain.entities.usuario import Usuario
from conn.db_conn import DBConn

class DataAccessUsuarioDAO(IDataAccessUsuarioDAO):

    def get(self, correo: str) -> Usuario:
        with self.__connect_to_mysql() as conn:           
            try:
                cursor = conn.cursor()
                query= "SELECT correo, nombres, apellidos, contasena, es_activo FROM usuario WHERE correo=%s"
                cursor.execute(query, (correo,))
                row = cursor.fetchone()
                if row:
                    return Usuario(row[0], row[1], row[2],row[3], row[4])
                return None
            except mysql.connector.Error as err:
                raise err
            

    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection