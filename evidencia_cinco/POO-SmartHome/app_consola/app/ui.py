from abc import ABC
from infraestructure.daos.mysql_usuario_dao import MySQLUsuarioDAO # Implementación concreta
from domain.entities.usuario import Usuario

# CONCEPTO IMPORTANTE: CLASES ESTATICAS
# Clase UI para manejar la interfaz de usuario en la consola
# Debe ser abstracta y no instanciable
# Contiene métodos estáticos para mostrar menús y obtener entradas del usuario
usuario1 = Usuario(id=1, correo="usuario1@example.com", nombres="Usuario", apellidos="Uno", contraseña="password123", es_activo=True)
class UI(ABC):

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
            return 'Iniciar sesión'
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
        contraseña = input("Ingrese su contraseña: ")
        # Crear una instancia del usuario, tal vez no sea la mejor idea. SOLO PARA PRUEBAS
        usuario = Usuario(correo=correo, nombres=nombre, apellidos=apellido, contraseña=contraseña, es_activo=True)
        return usuario