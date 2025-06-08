from auth import cambiar_rol, consultar_perfil, listar_usuarios, logout
from mensajes_consola import formatear_mensaje_consola
from dispositivos import buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, nuevo_dispositivo
from automatizaciones import cambiar_estado_automatizacion_aspiradora, consultar_automatizaciones_activas, iniciar_automatizacion_aspiradora, cambiar_estado_automatizacion_luces_del_patio, iniciar_automatizacion_luces_del_patio
from states import states


def mostrar_opciones_principal_de_app():
    if(states['is_auth']==False):
        print("1. Registrarse")
        print("2. Iniciar sesión")

   

def menu_automatizaciones():
    while True:
        print("1. Activar/desactivar automatizacion de luces del patio")
        print("2. Activar/desactivar aspiradora salon")
        print("0. Salir de automatizaciones")
        opcion2 = input("Ingrese una opcion: ")
        
        if(opcion2 == '1'):
            cambiar_estado_automatizacion_luces_del_patio()
            iniciar_automatizacion_luces_del_patio()
        elif(opcion2 == '2'):
            cambiar_estado_automatizacion_aspiradora()
            iniciar_automatizacion_aspiradora()
        elif(opcion2 == '0'):
            formatear_mensaje_consola("Saliste del menu automatizaciones")
            break

def mostrar_opciones_para_admin(): 
    #Permitir consultar automatizaciones activas
    #Gestionar dispositivos.
    #Permitir modificar el rol de un usuario. 
    print("1. Listar dispositivos")
    print("2. Registrar nuevo dispositivo")
    print("3. ELiminar un dispositivo")
    print("4. Buscar dispositivo")
    print("5. Consultar automatizaciones activas")
    print("6. Activar/desactivar automatizaciones")
    print("7. Listar Usuarios")
    print("8. Consultar Perfil")
    print("9. Cambiar Rol")
    print("10. Cerrar sesión")
    print("0. Salir")

def llamar_opciones_para_admin():
    opcion=input('Ingrese una opcion: ')
    if(opcion == '1'):
        listar_dispositivos()
    elif(opcion == '2'):
        nuevo_dispositivo()
    elif(opcion == '3'):
        eliminar_dispositivo()
    elif(opcion == '4'):
        buscar_dispositivo()                                
    elif(opcion == '5'):
        consultar_automatizaciones_activas()                                
    elif(opcion=="6"):
        menu_automatizaciones()                                
    elif(opcion=="7"):
        listar_usuarios()
    elif(opcion=="8"):
        consultar_perfil()
    elif(opcion=="9"):
        cambiar_rol()                                
    elif(opcion=="10"):
        logout()
    elif(opcion == '0'):
        print("Gracias vuelva pronto")
        return
                                

def mostrar_opciones_para_estandar():
    #Permitir consultar los datos personales.
    #Permitir activar/ejecutar/”configurar”(debería estar predefinida) la automatización.
    #Permitir consultar dispositivos.
    print("1. Listar dispositivos")
    print("2. Consultar Perfil")
    print("3. Consultar automatizaciones activas")
    print("4. Activar/desactivar automatizaciones")
    print("5. Cerrar sesión")
    print("0. Salir")

def llamar_opciones_para_estandar():
    opcion=input('Ingrese una opcion: ')
    if(opcion == '1'):
        listar_dispositivos()
    elif(opcion == '2'):
        consultar_perfil()
    elif(opcion == '3'):
        consultar_automatizaciones_activas()
    elif(opcion == '4'):
        menu_automatizaciones()
    elif(opcion == '5'):
        logout()
    elif(opcion == '0'):
        print("Gracias vuelva pronto")    
        return
