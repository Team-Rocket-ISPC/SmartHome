from dao.usuario_dao import UsuarioDAO
from dao.tipo_dispositivo_dao import DataAccessTipoDispositivoDAO
from domain.entities.usuario import Usuario
from domain.entities.tipo_dispositivo import TipoDispositivo
from dao.dispositivo_dao import DispositivoDAO
from domain.entities.dispositivo import Dispositivo
from datetime import datetime
from presentation.menu_automatizacion import menu_automatizaciones
from dao.automatizacion_dao import AutomatizacionDAO

def menu_principal():
    print("\n===== SmartHome Solutions =====")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("0. Salir")
    return input("Seleccione una opción: ")

def menu_usuario_estandar(correo):
    print(f"\n--- Menú Usuario Estándar ({correo}) ---")
    print("1. Consultar mis datos")
    print("2. Consultar dispositivos")
    print("3. Crear vivienda (asignarse como Admin)")
    print("0. Cerrar sesión")
    return input("Seleccione una opción: ")

def menu_admin(correo):
    print(f"\n--- Menú Administrador ({correo}) ---")
    print("1. CRUD de usuarios")
    print("2. CRUD de dispositivos")
    print("3. CRUD de automatizaciones")
    print("4. Cambiar rol de usuario")
    print("0. Cerrar sesión")
    return input("Seleccione una opción: ")

def registrar_usuario(usuario_dao):
    print("\n--- Registro de nuevo usuario ---")
    correo = input("Correo: ").strip().lower()
    nombres = input("Nombre/s: ")
    apellidos = input("Apellido/s: ")
    contrasena = input("Contraseña: ")

    usuario = Usuario(correo, nombres, apellidos, contrasena)
    if usuario_dao.create(usuario):
        print("Usuario registrado correctamente (rol: Estándar por defecto)")
    else:
        print("Error al registrar usuario.")

def iniciar_sesion(usuario_dao):
    print("\n--- Inicio de sesión ---")
    correo = input("Correo: ").strip().lower()
    contrasena = input("Contraseña: ")
    usuario = usuario_dao.get(correo)

    if usuario and usuario.contrasena == contrasena:
        print(f"Bienvenido {usuario.nombres}!")
        # acá verificar roles asociados más adelante
        if correo == "cristian@gmail.com":  # admin global
            return "Admin", correo
        else:
            return "Estandar", correo
    else:
        print("Credenciales incorrectas.")
        return None, None

def crud_usuarios(usuario_dao):
    while True:
        print("\n--- Gestión de usuarios ---")
        print("1. Listar usuarios")
        print("2. Buscar usuario por correo")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Volver")
        op = input("Opción: ")

        if op == "1":
            usuarios = usuario_dao.get_all()
            for u in usuarios:
                print(u)
        elif op == "2":
            correo = input("Correo: ").strip().lower()
            u = usuario_dao.get(correo)
            print(u if u else "Usuario no encontrado.")
        elif op == "3":
            correo = input("Correo del usuario a actualizar: ").strip().lower()
            u = usuario_dao.get(correo)      
            resultado = usuario_dao.update(u)
            if resultado:
                print("Usuario actualizado.")
            else:
                print("Error al actualizar usuario.")
        elif op == "4":
            correo = input("Correo del usuario a eliminar: ").strip().lower()
            resultado = usuario_dao.delete(correo)
            if resultado:
                print("Usuario eliminado.")
            else:
                print("Error al eliminar usuario.")
        elif op == "0":
            break
        else:
            print("Opción inválida.")

def crud_dispositivos(dao: DispositivoDAO):
    while True:
        print("\n--- Gestión de dispositivos ---")
        print("1. Listar dispositivos")
        print("2. Buscar dispositivo por ID")
        print("3. Crear dispositivo")
        print("4. Actualizar dispositivo")
        print("5. Encender/Apagar dispositivo")
        print("6. Eliminar dispositivo")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            dispositivos = dao.get_all()
            if dispositivos:
                print("\n📋 Lista de dispositivos:")
                for d in dispositivos:
                    print(d)
            else:
                print("No hay dispositivos registrados.")

        elif opcion == "2":
            try:
                id_disp = int(input("Ingrese ID del dispositivo: "))
                d = dao.get_by_id(id_disp)
                print(d if d else "Dispositivo no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            print("\n--- Crear nuevo dispositivo ---")
            nombre = input("Nombre del dispositivo: ").strip()
            estado = False  # Por defecto apagado
            id_tipo = int(input("ID del tipo de dispositivo: "))
            id_ubicacion = int(input("ID de la ubicación: "))
            fecha_hora = datetime.now()

            nuevo = Dispositivo(
                nombre=nombre,
                estado=estado,
                fecha_hora=fecha_hora,
                id_tipo=id_tipo,
                id_ubicacion=id_ubicacion
            )

            if dao.create(nuevo):
                print("✅ Dispositivo registrado correctamente.")
            else:
                print("❌ Error al crear el dispositivo.")

        elif opcion == "4":
            try:
                id_disp = int(input("Ingrese ID del dispositivo a actualizar: "))
                d = dao.get_by_id(id_disp)
                if d:
                    print(f"Editando {d.nombre}")
                    d.nombre = input(f"Nuevo nombre ({d.nombre}): ") or d.nombre
                    estado_input = input(f"Nuevo estado (1=Encendido, 0=Apagado, actual {int(d.estado)}): ")
                    if estado_input in ["0", "1"]:
                        d.estado = bool(int(estado_input))
                    d.id_tipo = int(input(f"Nuevo ID tipo ({d.id_tipo}): ") or d.id_tipo)
                    d.id_ubicacion = int(input(f"Nuevo ID ubicación ({d.id_ubicacion}): ") or d.id_ubicacion)
                    d.fecha_hora = datetime.now()
                    if dao.update(d):
                        print("✅ Dispositivo actualizado.")
                    else:
                        print("❌ Error al actualizar.")
                else:
                    print("Dispositivo no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "5":
            try:
                id_disp = int(input("Ingrese ID del dispositivo a encender/apagar: "))
                d = dao.get_by_id(id_disp)
                if d:
                    d.encender_apagar()
                else:
                    print("Dispositivo no encontrado.")
            except ValueError:
                print("ID inválido.")
                
        elif opcion == "6":
            try:
                id_disp = int(input("Ingrese ID del dispositivo a eliminar: "))
                if dao.delete(id_disp):
                    print("🗑️ Dispositivo eliminado correctamente.")
                else:
                    print("❌ Error al eliminar el dispositivo.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def main():
    usuario_dao = UsuarioDAO()
    dao = DispositivoDAO()
    auto_dao = AutomatizacionDAO()

    while True:
        opcion = menu_principal()
        if opcion == "1":
            registrar_usuario(usuario_dao)
        elif opcion == "2":
            rol, correo = iniciar_sesion(usuario_dao)
            if rol == "Admin":
                while True:
                    op_admin = menu_admin(correo)
                    if op_admin == "1":
                        crud_usuarios(usuario_dao)
                    elif op_admin == "2":
                        crud_dispositivos(dao)
                    elif op_admin == "3":
                        menu_automatizaciones(auto_dao)
                    elif op_admin == "4":
                        print("Cambio de rol (pendiente)")
                    elif op_admin == "0":
                        break
                    else:
                        print("Opción inválida.")
            elif rol == "Estandar":
                while True:
                    op_est = menu_usuario_estandar(correo)
                    if op_est == "1":
                        u = usuario_dao.get(correo)
                        print(u)
                    elif op_est == "2":
                        dispositivos = dao.get_all()
                        if dispositivos:
                            print("\nLista de dispositivos:")
                            for d in dispositivos:
                                print(d)
                        else:
                            print("No hay dispositivos registrados.")
                    elif op_est == "3":
                        print("Creación de vivienda (pendiente)")
                    elif op_est == "0":
                        break
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    




"""
PRUEBAS DEL DAO TIPO DISPOSITIVO 
    #para probar el tipo_dispositivo_dao directamente
if __name__ == "__main__":
    dao = DataAccessTipoDispositivoDAO()
    
    # GET ALL
    todos_tipos = dao.get_all()
    for tipo in todos_tipos:
        print(tipo.id_tipo, tipo.nombre)

    # Create
    nuevo_tipo = TipoDispositivo(nombre="Sensor de movimiento")
    creado = dao.create(nuevo_tipo)
    print("Creado:", creado.id_tipo, creado.nombre)

    # Get
    tipo_obtenido = dao.get(5)
    print(tipo_obtenido.id_tipo, tipo_obtenido.nombre)
   
    # Actualizar
    tipo_obtenido.nombre = "sensor actualizado"
    dao.update(tipo_obtenido)
    tipo_actualizado = dao.get(tipo_obtenido.id_tipo)
    print(tipo_actualizado.nombre)  # Debe decir "sensor actualizado"

    # Borrar
    dao.delete(tipo_actualizado.id_tipo)
    tipo_borrado = dao.get(tipo_actualizado.id_tipo)
    print(tipo_borrado)  # Debe ser None
"""