from typing import List, Optional
from conn.db_conn import DBConn
from domain.entities.ubicacion import Ubicacion
from dao.interfaces.interface_ubicacion_dao import IDataAccessUbicacionDAO
import mysql.connector
from abc import ABC

class UbicacionDAO(IDataAccessUbicacionDAO, ABC):

    def __connect_to_mysql(self):
        db = DBConn()
        return db.connect()

    def create(self, ubicacion: Ubicacion) -> bool:
        """Inserta una nueva ubicación en la base de datos (id_ubicacion autoincremental)."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO UBICACION (nombre, id_vivienda)
                    VALUES (%s, %s)
                """
                valores = (ubicacion.nombre, ubicacion.id_vivienda)
                cursor.execute(sql, valores)
                conexion.commit()
                ubicacion.id_ubicacion = cursor.lastrowid  # Asignar el ID autoincremental generado
                print(f"✅ Ubicación creada con ID: {ubicacion.id_ubicacion}")
                return True
            except mysql.connector.Error as e:
                print(f"[DAO] Error al crear ubicación: {e}")
                conexion.rollback()
                return False

    def get_all(self) -> List[Ubicacion]:
        """Obtiene una lista de todas las ubicaciones registradas."""
        with self.__connect_to_mysql() as conexion:
            ubicaciones = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_ubicacion, nombre, id_vivienda FROM UBICACION")
                filas = cursor.fetchall()
                for f in filas:
                    ubicaciones.append(
                        Ubicacion(
                            id_ubicacion=f[0],
                            nombre=f[1],
                            id_vivienda=f[2]
                        )
                    )
                return ubicaciones
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener ubicaciones: {e}")
                return []
    #agregar metodo get_by_vivienda

    def get_by_vivienda(self, id_vivienda: int) -> List[Ubicacion]:
        """Obtiene una lista de ubicaciones filtradas por id_vivienda."""
        with self.__connect_to_mysql() as conexion:
            ubicaciones = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_ubicacion, nombre, id_vivienda FROM UBICACION WHERE id_vivienda = %s", (id_vivienda,))
                filas = cursor.fetchall()
                for f in filas:
                    ubicaciones.append(
                        Ubicacion(
                            id_ubicacion=f[0],
                            nombre=f[1],
                            id_vivienda=f[2]
                        )
                    )
                return ubicaciones
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener ubicaciones por vivienda: {e}")
                return []

    def get(self, id_ubicacion: int) -> Optional[Ubicacion]:
        """Obtiene una ubicación específica por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_ubicacion, nombre, id_vivienda FROM UBICACION WHERE id_ubicacion = %s", (id_ubicacion,))
                f = cursor.fetchone()
                if f:
                    return Ubicacion(
                        id_ubicacion=f[0],
                        nombre=f[1],
                        id_vivienda=f[2]
                    )
                return None
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener ubicación por ID: {e}")
                return None

    def update(self, ubicacion: Ubicacion) -> bool:
        """Actualiza los datos de una ubicación existente."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    UPDATE UBICACION
                    SET nombre = %s, id_vivienda = %s
                    WHERE id_ubicacion = %s
                """
                valores = (ubicacion.nombre, ubicacion.id_vivienda, ubicacion.id_ubicacion)
                cursor.execute(sql, valores)
                conexion.commit()
                return cursor.rowcount > 0  # Verificar si se actualizó algo
            except mysql.connector.Error as e:
                print(f"[DAO] Error al actualizar ubicación: {e}")
                conexion.rollback()
                return False

    def delete(self, id_ubicacion: int) -> bool:
        """Elimina una ubicación de la base de datos."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM UBICACION WHERE id_ubicacion = %s", (id_ubicacion,))
                conexion.commit()
                return cursor.rowcount > 0  # Verificar si se eliminó alguna fila
            except mysql.connector.Error as e:
                print(f"[DAO] Error al eliminar ubicación: {e}")
                conexion.rollback()
                return False
