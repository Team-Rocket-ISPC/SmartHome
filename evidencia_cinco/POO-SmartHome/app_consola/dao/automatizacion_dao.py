from conn.db_conn import DBConn
from domain.entities.automatizacion import Automatizacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo
from domain.entities.tipo_dispositivo import TipoDispositivo
from domain.entities.ubicacion import Ubicacion
from dao.automatizacion_objetivo_dao import AutomatizacionObjetivoDAO
from dao.interfaces.interface_automatizacion_dao import IDataAccessAutomatizacionDAO

class AutomatizacionDAO(IDataAccessAutomatizacionDAO):
    """Implementación del DAO para la entidad Automatización."""
    def create(self, automatizacion: Automatizacion) -> bool:
        """Crea una nueva automatización en la base de datos junto con sus objetivos."""
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                 # Insertar la automatización principal
                sql_auto = """
                    INSERT INTO automatizaciones (nombre, id_vivienda, hora_inicio, hora_fin, activa)
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
                if not automatizacion.objetivos:
                    print("Advertencia: la automatización no tiene objetivos definidos.")
                else:
                    for obj in automatizacion.objetivos:
                        sql_obj = """
                            INSERT INTO automatizacion_objetivo (id_automatizacion, id_tipo, id_ubicacion)
                            VALUES (%s, %s, %s)
                        """
                        valores_obj = (
                            automatizacion.id_automatizacion,
                            obj.tipo_dispositivo.id_tipo,
                            obj.ubicacion.id_ubicacion
                        )
                        cursor.execute(sql_obj, valores_obj)

                conn.commit()
                print("Automatización creada correctamente.")
                return True

            except Exception as e:
                conn.rollback()
                print(f"Error al crear automatización: {e}")
                return False
       
    def get(self, id_automatizacion: int) -> Automatizacion | None:
        """Obtiene una automatización por su ID."""
        with self.__connect_to_mysql() as conn:
            if not conn:
                return None
            try:
                cursor = conn.cursor(dictionary=True)
                sql_auto = "SELECT * FROM automatizaciones WHERE id_automatizacion = %s"
                cursor.execute(sql_auto, (id_automatizacion,))
                row = cursor.fetchone()
                if not row:
                    return None

                automatizacion = Automatizacion(
                    id_automatizacion=row["id_automatizacion"],
                    nombre=row["nombre"],
                    id_vivienda=row["id_vivienda"],
                    hora_inicio=row["hora_inicio"],
                    hora_fin=row["hora_fin"],
                    activa=bool(row["activa"]),
                )

                # Reutilizo el DAO de objetivos
                objetivo_dao = AutomatizacionObjetivoDAO()
                objetivos = objetivo_dao.get(id_automatizacion)
                # Asigno la automatización padre a cada objetivo
                for obj in objetivos:
                    obj.automatizacion = automatizacion
                automatizacion.objetivos = objetivos
                return automatizacion

            except Exception as e:
                print(f"Error al obtener automatización: {e}")
                return None
   

    def get_all(self, id_vivienda: int = None) -> list[Automatizacion]:
        """Obtiene todas las automatizaciones, opcionalmente filtradas por ID de vivienda."""
        automatizaciones = []
        with self.__connect_to_mysql() as conn:
            if not conn:
                return []
            try:
                cursor = conn.cursor(dictionary=True)

                # Traigo todas o las filtradas por vivienda
                if id_vivienda:
                    sql = "SELECT * FROM automatizaciones WHERE id_vivienda = %s"
                    cursor.execute(sql, (id_vivienda,))
                else:
                    sql = "SELECT * FROM automatizaciones"
                    cursor.execute(sql)

                registros = cursor.fetchall()

                for r in registros:
                    # Creo la automatización
                    auto = Automatizacion(
                        id_automatizacion=r["id_automatizacion"],
                        nombre=r["nombre"],
                        id_vivienda=r["id_vivienda"],
                        hora_inicio=r["hora_inicio"],
                        hora_fin=r["hora_fin"],
                        activa=bool(r["activa"])
                    )

                    # Traigo los objetivos asociados
                    objetivo_dao = AutomatizacionObjetivoDAO()
                    objetivos = objetivo_dao.get(r["id_automatizacion"])

                    # Asigno correctamente los objetivos a la automatización
                    auto.objetivos = []
                    for obj in objetivos:
                        obj.automatizacion = auto  # Reasigno referencia
                        auto.objetivos.append(obj)

                    automatizaciones.append(auto)

                return automatizaciones

            except Exception as e:
                print(f"Error al obtener automatizaciones: {e}")
                return []
          
           
            
    def update(self, automatizacion: Automatizacion) -> bool:
        """Actualiza los datos de una automatización existente."""
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                # Pedimos nuevos valores
                nombre = input("Nuevo nombre de automatizacion (Enter para mantener): ").strip()
                id_vivienda = input("Nuevo id de vivienda (Enter para mantener): ").strip()
                hora_inicio = input("Nueva hora de inicio (Enter para mantener): ").strip()
                hora_fin = input("Nueva hora de fin (Enter para mantener): ").strip()
                activa = input("Nueva estado (1 para activa, 0 para inactiva) (Enter para mantener): ").strip()

                # Si el usuario no escribió nada, se mantiene el valor anterior
                if nombre:
                    automatizacion.nombre = nombre
                if id_vivienda:
                    automatizacion.id_vivienda = id_vivienda
                if hora_inicio:
                    automatizacion.hora_inicio = hora_inicio
                if hora_fin:
                    automatizacion.hora_fin = hora_fin
                if activa:
                    automatizacion.activa = bool(int(activa))

                sql = """
                    UPDATE automatizaciones
                    SET nombre=%s, id_vivienda=%s, hora_inicio=%s, hora_fin=%s, activa=%s
                    WHERE id_automatizacion=%s
                """
                valores = (
                    automatizacion.nombre,
                    automatizacion.id_vivienda,
                    automatizacion.hora_inicio,
                    automatizacion.hora_fin,
                    int(automatizacion.activa),
                    automatizacion.id_automatizacion
                )
                cursor.execute(sql, valores)
                conn.commit()
                print("Automatización actualizada correctamente.")
                return True

            except Exception as e:
                print(f"Error al obtener automatizaciones: {e}")
                return []

    def delete(self, id_automatizacion: int) -> bool:
        """Elimina una automatización por su ID."""
        with self.__connect_to_mysql() as conn:
            if not conn:
                return False
            try:
                cursor = conn.cursor()
                # Primero elimino los objetivos asociados
                sql_obj = "DELETE FROM automatizacion_objetivo WHERE id_automatizacion = %s"
                cursor.execute(sql_obj, (id_automatizacion,))
                if cursor.rowcount == 0:
                    print("No se encontraron objetivos asociados a la automatización.")
                # Luego elimino la automatización
                sql_auto = "DELETE FROM automatizaciones WHERE id_automatizacion = %s"
                cursor.execute(sql_auto, (id_automatizacion,))
                conn.commit()
                print("Automatización eliminada correctamente.")
                return True

            except Exception as e:
                print(f"Error al eliminar automatización: {e}")
                return False

    def __connect_to_mysql(self):
        """Establece una conexión con la base de datos MySQL."""
        db = DBConn()
        connection = db.connect()  
        return connection
    
"""
# Ejemplo de uso Create:
# Se crea la automatización (se pide por consola nombre id vivienda hora inicio y hora fin)
# auto = Automatizacion("Modo Noche", id_vivienda=1, hora_inicio="22:00", hora_fin="06:00", activa=True)
# Se agregan los objetivos (aca por consola hay que mostrar los tipos y ubicaciones disponibles para elegir segun id vivienda)
# Cuando el usuario elija tipo y ubicacion, se crean dichos objetos:
# obj1 = AutomatizacionObjetivo(auto, tipo_dispositivo=TipoDispositivo(1, "Luz"), ubicacion=Ubicacion(2, "Dormitorio", 1)) 
# obj2 = AutomatizacionObjetivo(auto, tipo_dispositivo=TipoDispositivo(2, "Aire"), ubicacion=Ubicacion(3, "Living", 1)) 
# Se guardan los objetivos dentro del objeto automatización 
# auto.objetivos.append(obj1) 
# auto.objetivos.append(obj2) 
# Ahora se envía todo junto al DAO 
# dao = automatizacion_dao() 
# dao.create(auto) --> aca auto ya tiene sus objetivos asociados

"""