from dao.automatizacion_dao import AutomatizacionDAO
from dao.tipo_dispositivo_dao import DataAccessTipoDispositivoDAO
#from dao.ubicacion_dao import UbicacionDao  #Falta Crear UbicacionDao
from domain.entities.automatizacion import Automatizacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo
from domain.entities.tipo_dispositivo import TipoDispositivo
from domain.entities.ubicacion import Ubicacion


def menu_automatizaciones(auto_dao):
    while True:
        print("\n=== MENÚ AUTOMATIZACIONES ===")
        print("1. Listar todas las automatizaciones")
        print("2. Listar automatizaciones por vivienda")
        print("3. Crear automatización")
        print("4. Modificar automatización")
        print("5. Eliminar automatización")
        print("0. Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            automatizaciones = auto_dao.get_all()
            if automatizaciones:
                for a in automatizaciones:
                    print(a)
            else:
                print("No hay automatizaciones registradas.")
        
        elif opcion == "2":
            id_viv = input("Ingrese el ID de la vivienda: ")
            automatizaciones = auto_dao.get_all(id_vivienda=int(id_viv))
            if automatizaciones:
                for a in automatizaciones:
                    print(a)
            else:
                print("No hay automatizaciones para esa vivienda.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def crear_automatizacion(auto_dao):
    print("\n--- Crear nueva automatización ---")

    nombre = input("Nombre de la automatización: ")
    id_vivienda = int(input("ID de la vivienda: ")) #Esto deberia sugerir las viviendas del usuario logueado
    hora_inicio = input("Hora de inicio (HH:MM): ")
    hora_fin = input("Hora de fin (HH:MM): ")

    auto = Automatizacion(nombre, id_vivienda, hora_inicio, hora_fin, activa=True)

    print("\n--- Agregar objetivos ---")
    tipo_dao = DataAccessTipoDispositivoDAO()
    ubic_dao = UbicacionDao() #Falta Crear UbicacionDao

    while True:
        # Mostrar tipos de dispositivo disponibles
        tipos = tipo_dao.get_all()
        print("\nTipos de dispositivo disponibles:")
        for t in tipos:
            print(f"{t.id_tipo} - {t.nombre}")

        id_tipo = int(input("Seleccione el ID de tipo de dispositivo (0 para terminar): "))
        if id_tipo == 0:
            break

        # Mostrar ubicaciones disponibles
        ubicaciones = ubic_dao.get_by_vivienda(id_vivienda)
        print("\nUbicaciones en la vivienda:")
        for u in ubicaciones:
            print(f"{u.id_ubicacion} - {u.nombre}")

        id_ubicacion = int(input("Seleccione el ID de la ubicación: "))

        # Crear los objetos de dominio
        tipo_dao = DataAccessTipoDispositivoDAO()
        ubic_dao = UbicacionDao()

        tipo = tipo_dao.get(id_tipo)
        ubic = ubic_dao.get(id_ubicacion)



        # Crear el objetivo (se agrega solo a auto.objetivos)
        AutomatizacionObjetivo(auto, tipo, ubic)

        seguir = input("¿Agregar otro objetivo? (s/n): ").lower()
        if seguir != "s":
            break

    dao = AutomatizacionDAO()
    dao.create(auto)

def listar_automatizaciones(auto_dao):
    print("\n--- Listado de automatizaciones ---")
    id_vivienda = int(input("Ingrese el ID de la vivienda para filtrar (solo enter para ver todas): "))
   

    if not automatizaciones:
        print("No hay automatizaciones registradas.")
        return

    for a in automatizaciones:
        estado = "Activa" if a.activa else "Inactiva"
        print(f"ID: {a.id_automatizacion}, Nombre: {a.nombre}, Vivienda: {a.id_vivienda}, "
              f"Horario: {a.hora_inicio} - {a.hora_fin}, Estado: {estado}")
        if a.objetivos:
            print("  Objetivos:")
            for obj in a.objetivos:
                print(f"    - Tipo: {obj.tipo_dispositivo.nombre}, Ubicación: {obj.ubicacion.nombre}")
        else:
            print("  No tiene objetivos definidos.")