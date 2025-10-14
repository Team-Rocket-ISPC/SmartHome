from typing import List, Optional
from conn.db_conn import DBConn
from domain.entities.accion import Accion
import mysql.connector  # Captura de errores específicos
from interfaces.interface_accion_dao import IDataAccesAccionDAO

class AccionDAO(IDataAccesAccionDAO):
    """Implementación del DAO para la entidad Acción."""
    def create(self, accion: Accion) -> bool:
        """Crea una nueva acción en la base de datos."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO ACCION (nombre, id_tipo)
                    VALUES (%s, %s)
                """
                valores = (accion.nombre, accion.id_tipo)
                cursor.execute(sql, valores)
                conexion.commit()
                accion.id_accion = cursor.lastrowid
                print(f"✅ Acción creada con ID: {accion.id_accion}")
                return True
            except mysql.connector.Error as e:
                print(f"[DAO] Error al crear acción: {e}")
                conexion.rollback()
                return False

    def get_all(self) -> List[Accion]:
        """Obtiene todas las acciones de la base de datos."""
        with self.__connect_to_mysql() as conexion:
            acciones = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_accion, nombre, id_tipo FROM ACCION")
                filas = cursor.fetchall()
                for f in filas:
                    acciones.append(Accion(id_accion=f[0], nombre=f[1], id_tipo=f[2]))
                return acciones
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener acciones: {e}")
                return []


    def get_by_tipo(self, id_tipo: int) -> List[Accion]:
        """Obtiene acciones de la base de datos por tipo."""
        with self.__connect_to_mysql() as conexion:
            acciones = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_accion, nombre, id_tipo FROM ACCION WHERE id_tipo = %s", (id_tipo,))
                filas = cursor.fetchall()
                for f in filas:
                    acciones.append(Accion(id_accion=f[0], nombre=f[1], id_tipo=f[2]))
                return acciones
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener acciones por tipo: {e}")
                return []


    def get_by_id(self, id_accion: int) -> Optional[Accion]:
        """Obtiene una acción de la base de datos por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_accion, nombre, id_tipo FROM ACCION WHERE id_accion = %s", (id_accion,))
                f = cursor.fetchone()
                if f:
                    return Accion(id_accion=f[0], nombre=f[1], id_tipo=f[2])
                return None
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener acción por ID: {e}")
                return None

    def update(self, accion: Accion) -> bool:
        """Actualiza una acción existente en la base de datos."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    UPDATE ACCION SET nombre = %s, id_tipo = %s
                    WHERE id_accion = %s
                """
                valores = (accion.nombre, accion.id_tipo, accion.id_accion)
                cursor.execute(sql, valores)
                conexion.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as e:
                print(f"[DAO] Error al actualizar acción: {e}")
                conexion.rollback()
                return False

    def delete(self, id_accion: int) -> bool:
        """Elimina una acción de la base de datos por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM ACCION WHERE id_accion = %s", (id_accion,))
                conexion.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as e:
                print(f"[DAO] Error al eliminar acción: {e}")
                conexion.rollback()
                return False

    def __connect_to_mysql(self):
        """Establece una conexión con la base de datos MySQL."""
        db = DBConn()
        connection = db.connect()  
        return connection