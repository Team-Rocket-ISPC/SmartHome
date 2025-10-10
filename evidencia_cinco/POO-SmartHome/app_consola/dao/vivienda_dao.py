from typing import List, Optional
from conn.db_conn import DBConn
from domain.vivienda import Vivienda
import mysql.connector
from abc import ABC

class ViviendaDAO(IViviendaDAO, ABC):

    def __connect_to_mysql(self):
        db = DBConn()
        return db.connect()

    def create(self, vivienda: Vivienda) -> bool:
        """Inserta una nueva vivienda en la base de datos (id_vivienda autoincremental)."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO VIVIENDA (direccion, codigo_postal, id_vivienda)
                    VALUES (%s, %s, %s)
                """
                valores = (
                    vivienda.direccion,
                    vivienda.codigo_postal,
                    vivienda.id_vivienda
    
                )
                cursor.execute(sql, valores)
                conexion.commit()
                vivienda.id_vivienda = cursor.lastrowid  # Asignar el ID generado
                print(f"✅ Vivienda creada con ID: {vivienda.id_vivienda}")
                return True
            except mysql.connector.Error as e:
                print(f"[DAO] Error al crear vivienda: {e}")
                conexion.rollback()
                return False

    def get_all(self) -> List[Vivienda]:
        """Obtiene una lista de todas las viviendas registradas."""
        with self.__connect_to_mysql() as conexion:
            viviendas = []
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_vivienda, direccion, codigo_postal FROM VIVIENDA")
                filas = cursor.fetchall()
                for f in filas:
                    viviendas.append(
                        Vivienda(
                            id_vivienda=f[0],
                            direccion=f[1],
                            codigo_postal=f[2]
                        )
                    )
                return viviendas
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener viviendas: {e}")
                return []

    def get(self, id_vivienda: int) -> Optional[Vivienda]:
        """Obtiene una vivienda específica por su ID."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_vivienda, direccion, codigo_postal FROM VIVIENDA WHERE id_vivienda = %s", (id_vivienda,))
                f = cursor.fetchone()
                if f:
                    return Vivienda(
                        id_vivienda=f[0],
                        direccion=f[1],
                        codigo_postal=f[2]
                    )
                return None
            except mysql.connector.Error as e:
                print(f"[DAO] Error al obtener vivienda por ID: {e}")
                return None

    def update(self, vivienda: Vivienda) -> bool:
        """Actualiza los datos de una vivienda existente."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                sql = """
                    UPDATE VIVIENDA
                    SET direccion = %s, codigo_postal = %s
                    WHERE id_vivienda = %s
                """
                valores = (
                    vivienda.direccion,
                    vivienda.codigo_postal,
                    vivienda.id_vivienda
                )
                cursor.execute(sql, valores)
                conexion.commit()
                return cursor.rowcount > 0  # Verificar si se actualizó algo
            except mysql.connector.Error as e:
                print(f"[DAO] Error al actualizar vivienda: {e}")
                conexion.rollback()
                return False

    def delete(self, id_vivienda: int) -> bool:
        """Elimina una vivienda de la base de datos."""
        with self.__connect_to_mysql() as conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM VIVIENDA WHERE id_vivienda = %s", (id_vivienda,))
                conexion.commit()
                return cursor.rowcount > 0  # Verificar si se eliminó alguna fila
            except mysql.connector.Error as e:
                print(f"[DAO] Error al eliminar vivienda: {e}")
                conexion.rollback()
                return False
