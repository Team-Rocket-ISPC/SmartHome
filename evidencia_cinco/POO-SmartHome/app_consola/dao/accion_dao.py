from typing import List, Optional
from conn.db_conn import DBConn
from domain.entities.accion import Accion
import mysql.connector  # Captura de errores específicos

class AccionDAO:
    # 🔹 Crear una nueva acción
    def create(self, accion: Accion) -> bool:
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

    # 🔹 Obtener todas las acciones
    def get_all(self) -> List[Accion]:
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

    # 🔹 Obtener acciones por tipo de dispositivo
    def get_by_tipo(self, id_tipo: int) -> List[Accion]:
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

    # 🔹 Obtener una acción por ID
    def get_by_id(self, id_accion: int) -> Optional[Accion]:
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

    # 🔹 Actualizar una acción existente
    def update(self, accion: Accion) -> bool:
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

    # 🔹 Eliminar una acción
    def delete(self, id_accion: int) -> bool:
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

    # 🔹 Conexión con la base de datos
    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection