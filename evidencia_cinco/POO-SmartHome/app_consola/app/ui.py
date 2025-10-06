from abc import ABC
import re
from infraestructure.dao.mysql_usuario_dao import MySQLUsuarioDAO # Implementación concreta
from infraestructure.dao.mysql_usuario_autorizacion_dao import MySQLUsuarioAutorizacionDAO # Implementación concreta
from domain.entities.usuario import Usuario

class UI(ABC):
    """Clase abstracta para la interfaz de usuario en consola.
    Contiene métodos estáticos para mostrar menús, obtener y validar entradas del usuario.
    No se puede instanciar directamente."""

    def __new__(cls):
        if cls is UI:
            raise TypeError("No se puede instanciar la clase abstracta UI directamente.")
        return super().__new__(cls)

    @staticmethod
    def mostrar_menu_principal():
        print("=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
    
    @staticmethod
    def ejecutar_menu_principal():
        UI.mostrar_menu_principal()
        opcion = UI.obtener_opcion()
        if opcion == '1':
            usuario = UI.obtener_datos_usuario()
            # Crear una instancia del repositorio
            repo = MySQLUsuarioDAO()  # Cambiado a la implementación concreta
            repo.agregar_usuario(usuario)
            return 'Registro completado'
        elif opcion == '2':
            datos = UI.iniciar_sesion()
            repo = MySQLUsuarioAutorizacionDAO()  # Cambiado a la implementación concreta
            usuario = repo.autorizar_usuario(datos[0], datos[1])
            if usuario and usuario.is_auth:
                print("Inicio de sesión exitoso.")
                # Aquí puedes agregar lógica adicional para el usuario autenticado
                #Aca deberia llamar a un nuevo menu para otra tarea
                UI.mostrar_menu_estandar()
                opcion = UI.obtener_opcion()
                if opcion == '1':
                    print(usuario)
                elif opcion == '2':
                    print("Consultando dispositivos...")
                elif opcion == '3':
                    print("Cerrando sesión...")
                else:
                    print("Opción no válida.")

                return 'Inicio de sesión completado'
            else:
                print("Inicio de sesión fallido.")
                return 'Inicio de sesión fallido'
        elif opcion == '3':
            return 'Salir'
        else:
            print("Opción no válida. Intente de nuevo.")
            return UI.ejecutar_menu_principal()

    @staticmethod
    def obtener_opcion():
        opcion = input("Seleccione una opción: ")
        return opcion
    
    @staticmethod
    def obtener_datos_usuario():
        print("=== Registro. Inserte sus datos ===")
        correo = input("Ingrese su correo: ")
        nombre = input("Ingrese su/s nombre/s: ")
        apellido = input("Ingrese su/s apellido/s: ")
        contrasena = input("Ingrese su contraseña: ")


        if UI.validar_entrada(correo, nombre, apellido, contrasena):
            usuario = Usuario(correo=correo, nombres=nombre, apellidos=apellido, contrasena=contrasena, es_activo=True)
            return usuario
        else:
            return UI.obtener_datos_usuario()
        
    @staticmethod
    def validar_entrada(correo, nombre, apellido, contraseña):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print("Correo inválido. Revise formato.")
            return UI.obtener_datos_usuario()
        if len(nombre) < 3 or not nombre:
            print("El nombre debe tener al menos 3 caracteres.")
            return UI.obtener_datos_usuario()
        if len(apellido) < 3 or not apellido:
            print("El apellido debe tener al menos 3 caracteres.")
            return UI.obtener_datos_usuario()
        if len(contraseña) < 4 or not contraseña:
            print("La contraseña debe tener al menos 4 caracteres.")
            return UI.obtener_datos_usuario()
        else:
            return True
        
    @staticmethod
    def iniciar_sesion():
        print("=== Iniciar sesión ===")
        correo = input("Ingrese su correo: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print("Correo inválido. Revise formato.")
            return UI.obtener_datos_usuario()
        contrasena = input("Ingrese su contraseña: ")
        if len(contrasena) < 4 or not contrasena:
            print("La contraseña debe tener al menos 4 caracteres.")
            return UI.obtener_datos_usuario()
        return correo, contrasena
    
    @staticmethod
    def mostrar_menu_estandar():
        print("=== Menú Estándar ===")
        print("1. Consultar datos personales.")
        print("2. Consultar dispositivos")
        print("3. Cerrar sesión")
    