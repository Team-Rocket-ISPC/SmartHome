from conn.db_conn import DBConn
from domain.entities.automatizacion import Automatizacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo

class AutomatizacionDAO:

    def create(self, automatizacion: Automatizacion) -> bool:
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                 # Insertar la automatización principal
                sql_auto = """
                    INSERT INTO automatizacion (nombre, id_vivienda, hora_inicio, hora_fin, activa)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (
                    automatizacion.nombre,
                    automatizacion.id_vivienda, 
                    automatizacion.hora_inicio,
                    automatizacion.hora_fin,
                    int(automatizacion.activa)
                )
                cursor.execute(sql_auto, valores)
                conn.commit()

                # Obtener el ID autogenerado
                automatizacion.id_automatizacion = cursor.lastrowid

                # Insertar los objetivos asociados
                for obj in automatizacion.objetivos:
                    sql_obj = """
                        INSERT INTO automatizacion_objetivo (id_automatizacion, id_tipo, id_ubicacion)
                        VALUES (%s, %s, %s)
                    """
                    valores_obj = (
                        automatizacion.id_automatizacion,
                        obj.id_tipo,
                        obj.id_ubicacion
                    )
                    cursor.execute(sql_obj, valores_obj)

                conn.commit()
                print("✅ Automatización creada correctamente.")
                return True

            except Exception as e:
                conn.rollback()
                print(f"❌ Error al crear automatización: {e}")
                return False
       

    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection