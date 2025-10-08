from dao.usuario_dao import UsuarioDAO
from domain.entities.usuario import Usuario

def menu_principal():
    print("\n===== SmartHome Solutions =====")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("0. Salir")
    return input("Seleccione una opción: ")

def menu_usuario_estandar(correo):
    print(f"\n--- Menú Usuario Estándar ({correo}) ---")
    print("1. Consultar mis datos")
    print("2. Consultar dispositivos (pendiente)")
    print("3. Crear vivienda (asignarse como Admin)")
    print("0. Cerrar sesión")
    return input("Seleccione una opción: ")

def menu_admin(correo):
    print(f"\n--- Menú Administrador ({correo}) ---")
    print("1. CRUD de usuarios")
    print("2. Cambiar rol de usuario")
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

def main():
    usuario_dao = UsuarioDAO()

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
                        #Esto apunta a tabla USUARIO_VIVIENDA
                        print("Cambio de rol (pendiente)")
                    elif op_admin == "0":
                        break
            elif rol == "Estandar":
                while True:
                    op_est = menu_usuario_estandar(correo)
                    if op_est == "1":
                        u = usuario_dao.get(correo)
                        print(u)
                    elif op_est == "2":
                        #ESTO APUNTA A TABLA DISPOSITIVO
                        print("Consulta de dispositivos (pendiente)")
                    elif op_est == "3":
                        #ESTO APUNTA A TABLA VIVIENDA
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

