from typing import List, Optional
from conn.db_conn import DBConn
from domain.entities.dispositivo import Dispositivo
from dao.interfaces.interface_dispositivo_dao import IDataAccessDispositivoDAO 
from datetime import datetime
import mysql.connector  # Importar la librería para capturar errores específicos


class DispositivoDAO(IDataAccessDispositivoDAO):
    """Clase para manejar operaciones CRUD de Dispositivo en MySQL."""
    def create(self, dispositivo: Dispositivo) -> bool:
        """Crea un nuevo dispositivo en la base de datos."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO DISPOSITIVO (nombre, estado, fecha_hora, id_tipo, id_ubicacion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (
                    dispositivo.nombre,
                    dispositivo.estado,
                    dispositivo.fecha_hora,
                    dispositivo.id_tipo,
                    dispositivo.id_ubicacion
                )
                cursor.execute(sql, valores)
                conexion.commit()
                dispositivo.id_dispositivo = cursor.lastrowid  # Obtener el ID auto-incremental generado
                print(f"✅ Dispositivo creado con ID: {dispositivo.id_dispositivo}")
                return True
            except mysql.connector.Error as e:  # Capturar errores específicos de MySQL
                print(f"[DAO] Error al crear dispositivo: {e}")
                conexion.rollback()
                return False

    def get_all(self) -> List[Dispositivo]:
        """Obtiene todos los dispositivos de la base de datos."""
        with self.__connect_to_mysql() as conexion:
            dispositivos = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM DISPOSITIVO")
                filas = cursor.fetchall()
                for f in filas:
                    dispositivos.append(
                        Dispositivo(
                            id_dispositivo=f[0],  # El primer campo debería ser id_dispositivo
                            nombre=f[1],
                            estado=bool(f[2]),
                            fecha_hora=f[3],
                            id_tipo=f[4],
                            id_ubicacion=f[5]
                        )
                    )
                return dispositivos
            except mysql.connector.Error as e:  # Capturar errores específicos de MySQL
                print(f"[DAO] Error al obtener dispositivos: {e}")
                return []


    def get_by_id(self, id_dispositivo: int) -> Optional[Dispositivo]:
        """Obtiene un dispositivo por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM DISPOSITIVO WHERE id_dispositivo = %s", (id_dispositivo,))
                f = cursor.fetchone()
                if f:
                    return Dispositivo(
                        id_dispositivo=f[0],
                        nombre=f[1],
                        estado=bool(f[2]),
                        fecha_hora=f[3],
                        id_tipo=f[4],
                        id_ubicacion=f[5]
                    )
                return None
            except mysql.connector.Error as e:  # Capturar errores específicos de MySQL
                print(f"[DAO] Error al obtener dispositivo: {e}")
                return None


    def update(self, dispositivo: Dispositivo) -> bool:
        """Actualiza un dispositivo existente en la base de datos."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    UPDATE DISPOSITIVO
                    SET nombre = %s, estado = %s, fecha_hora = %s, id_tipo = %s, id_ubicacion = %s
                    WHERE id_dispositivo = %s
                """
                valores = (
                    dispositivo.nombre,
                    dispositivo.estado,
                    dispositivo.fecha_hora,
                    dispositivo.id_tipo,
                    dispositivo.id_ubicacion,
                    dispositivo.id_dispositivo
                )
                cursor.execute(sql, valores)
                conexion.commit()
                return cursor.rowcount > 0  # True si se modificó algo
            except mysql.connector.Error as e:  # Capturar errores específicos de MySQL
                print(f"[DAO] Error al actualizar dispositivo: {e}")
                conexion.rollback()
                return False


    def update_estado(self, id_dispositivo: int, nuevo_estado: bool) -> bool:
        """Actualiza solo el estado de un dispositivo."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    UPDATE DISPOSITIVO
                    SET estado = %s
                    WHERE id_dispositivo = %s
                """
                cursor.execute(sql, (nuevo_estado, id_dispositivo))
                conexion.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as e:
                print(f"[DAO] Error al actualizar estado: {e}")
                conexion.rollback()
                return False

    def delete(self, id_dispositivo: int) -> bool:
        """Elimina un dispositivo de la base de datos por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM DISPOSITIVO WHERE id_dispositivo = %s", (id_dispositivo,))
                conexion.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as e:  # Capturar errores específicos de MySQL
                print(f"[DAO] Error al eliminar dispositivo: {e}")
                conexion.rollback()
                return False
            

    def __connect_to_mysql(self):
        """Establece la conexión a la base de datos MySQL."""
        db = DBConn()
        return db.connect()