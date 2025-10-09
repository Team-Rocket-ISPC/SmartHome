from conn.db_conn import DBConn
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo
from domain.entities.tipo_dispositivo import TipoDispositivo
from domain.entities.ubicacion import Ubicacion

class automatizacion_objetivo_dao:
    def create(self, objetivo: AutomatizacionObjetivo) -> bool:
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                sql = """
                    INSERT INTO automatizacion_objetivo (id_automatizacion, id_tipo, id_ubicacion)
                    VALUES (%s, %s, %s)
                """
                valores = (
                    objetivo.automatizacion.id_automatizacion,
                    objetivo.tipo_dispositivo.id_tipo,
                    objetivo.ubicacion.id_ubicacion
                )
                cursor.execute(sql, valores)
                conn.commit()
                print(f"✅ Objetivo agregado a la automatización {objetivo.automatizacion.nombre}")
                return True
            except Exception as e:
                print(f"❌ Error al crear objetivo: {e}")
                conn.rollback()
                return False
   
    def get_all(self) -> list[AutomatizacionObjetivo]:
        with self.__connect_to_mysql() as conn:
           objetivos = []
           if not conn:
              return objetivos
           try:
               cursor = conn.cursor(dictionary=True)
               sql = """
                    SELECT ao.*, a.nombre AS automatizacion_nombre, 
                        t.id_tipo, t.nombre AS tipo_nombre, 
                        u.id_ubicacion, u.nombre AS ubicacion_nombre
                    FROM automatizacion_objetivo ao
                    JOIN automatizacion a ON ao.id_automatizacion = a.id_automatizacion
                    JOIN tipo_dispositivo t ON ao.id_tipo = t.id_tipo
                    JOIN ubicacion u ON ao.id_ubicacion = u.id_ubicacion
                """
               cursor.execute(sql)
               registros = cursor.fetchall()

               for r in registros:
                    tipo = TipoDispositivo(r["id_tipo"], r["tipo_nombre"])
                    ubicacion = Ubicacion(r["id_ubicacion"], r["ubicacion_nombre"], None)
                    objetivo = AutomatizacionObjetivo(
                        automatizacion=None,  # No reconstruimos toda la automatización aquí
                        tipo_dispositivo=tipo,
                        ubicacion=ubicacion
                    )
                    objetivos.append(objetivo)

               return objetivos
           except Exception as e:
                print(f"❌ Error al obtener objetivos: {e}")
                return []
        


    def get(self, id_automatizacion: int) -> list[AutomatizacionObjetivo]:
        with self.__connect_to_mysql() as conn:
           objetivos = []
           if not conn:
                return objetivos
           try:
                cursor = conn.cursor()
                sql = """
                    SELECT ao.*, t.id_tipo, t.nombre AS tipo_nombre,
                        u.id_ubicacion, u.nombre AS ubicacion_nombre
                    FROM automatizacion_objetivo ao
                    JOIN tipo_dispositivo t ON ao.id_tipo = t.id_tipo
                    JOIN ubicacion u ON ao.id_ubicacion = u.id_ubicacion
                    WHERE ao.id_automatizacion = %s
                """
                cursor.execute(sql, (id_automatizacion,))
                registros = cursor.fetchall()

                for r in registros:
                    tipo = TipoDispositivo(r["id_tipo"], r["tipo_nombre"])
                    ubicacion = Ubicacion(r["id_ubicacion"], r["ubicacion_nombre"], None)
                    objetivo = AutomatizacionObjetivo(
                        automatizacion=None,
                        tipo_dispositivo=tipo,
                        ubicacion=ubicacion
                    )
                    objetivos.append(objetivo)

                return objetivos
           except Exception as e:
                print(f"❌ Error al obtener objetivos por automatización: {e}")
                return []


    def delete(self, id_automatizacion: int, id_tipo: int, id_ubicacion: int) -> bool:
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                sql = """
                    DELETE FROM automatizacion_objetivo
                    WHERE id_automatizacion = %s AND id_tipo = %s AND id_ubicacion = %s
                """
                cursor.execute(sql, (id_automatizacion, id_tipo, id_ubicacion))
                conn.commit()
                print("Objetivo eliminado correctamente.")
                return True
            except Exception as e:
                print(f"❌ Error al eliminar objetivo: {e}")
                conn.rollback()
                return False
    

    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection