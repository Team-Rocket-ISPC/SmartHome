
import mysql.connector
from domain.entities.vivienda import Vivienda
from domain.repositories.vivienda_dao import IViviendaDao
from core.database import Database

# Implementación concreta de IViviendaDao para MySQL
class MySQLViviendaDAO(IViviendaDao):
    # Varible de clase, hace que todas las instancias compartan la misma conexión. No es lo mas adecuado.
    # conexion = Database().get_connection()
    # Sería mejor manejar la conexión en cada método o usar un patrón de diseño como Singleton

    def __init__(self):
        # Creo una instancia de la base de datos para cada DAO
        self.database = Database()

    def _get_connection(self):
        """Obtiene una nueva conexión para cada operación"""
        return self.database.get_connection()

    def agregar_vivienda(self, vivienda: Vivienda):
        """Agrega una nueva vivienda a la base de datos"""
        conexion = self._get_connection()
        if not conexion:
            print("No se pudo establecer la conexión a la base de datos.")
            return
        with conexion.cursor() as cursor:
            try:
                query = "INSERT INTO vivienda (id_vivienda, direccion, codigo_postal) VALUES (%s, %s, %s)"
                cursor.execute(query, (vivienda.id_vivienda, vivienda.direccion, vivienda.codigo_postal))
                conexion.commit()
                print(f"Vivienda agregada con exito: {vivienda.id_vivienda}")
            except mysql.connector.Error as err:
                print(f"Error al agregar vivienda: {err}")
                conexion.rollback()

    def obtener_vivienda(self, vivienda_id: int) -> Vivienda:
        """Obtiene una vivienda por su ID"""
        conexion = self._get_connection()
        if not conexion:
            print("No se pudo establecer la conexión a la base de datos.")
            return
        with conexion.cursor() as cursor:
            try:
                cursor = conexion.cursor(dictionary=True)
                query = "SELECT * FROM vivienda WHERE id_vivienda = %s"
                cursor.execute(query, (vivienda_id,))
                result = cursor.fetchone()
                if result:
                    return Vivienda(id_vivienda=result['id_vivienda'], direccion=result['direccion'], codigo_postal=result['codigo_postal'])
                else:
                    print("Vivienda no encontrada.")
                    return None
            except mysql.connector.Error as err:
                print(f"Error al obtener vivienda: {err}")
                return None
            finally:
                cursor.close()
                self.conexion.close()

    def eliminar_vivienda(self, vivienda_id: int):
        if self.conexion:
            try:
                cursor = self.conexion.cursor()
                query = "DELETE FROM vivienda WHERE id_vivienda = %s"
                cursor.execute(query, (vivienda_id,))
                self.conexion.commit()
                print(f"Vivienda eliminada con ID: {vivienda_id}")
            except mysql.connector.Error as err:
                print(f"Error al eliminar vivienda: {err}")
                self.conexion.rollback()
            finally:
                cursor.close()
                self.conexion.close()

    def listar_viviendas(self) -> list[Vivienda]:
        if self.conexion:
            try:
                cursor = self.conexion.cursor(dictionary=True)
                query = "SELECT * FROM vivienda"
                cursor.execute(query)
                results = cursor.fetchall()
                return [Vivienda(id_vivienda=row['id_vivienda'], direccion=row['direccion'], codigo_postal=row['codigo_postal']) for row in results]
            except mysql.connector.Error as err:
                print(f"Error al listar viviendas: {err}")
                return []
            finally:
                cursor.close()
                self.conexion.close()