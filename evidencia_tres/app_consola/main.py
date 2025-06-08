
from dispositivos import buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, nuevo_dispositivo
from menu import menu_automatizaciones, mostrar_opciones_principal_de_app, mostrar_opciones_para_admin, mostrar_opciones_para_estandar 
from automatizaciones import consultar_automatizaciones_activas, iniciar_automatizacion_aspiradora, iniciar_automatizacion_luces_del_patio
import datetime
from auth import verificar_rol, cambiar_rol, consultar_perfil, listar_usuarios, login, logout, register
from states import states
def main():
    print(f"----BIENVENIDO A SMART HOME SOLUTIONS----{datetime.datetime.now().strftime("%H:%M")}")
    iniciar_automatizacion_aspiradora()
    iniciar_automatizacion_luces_del_patio()
    while True:
        mostrar_opciones_principal_de_app()
       
        opcion=input('Ingrese una opcion: ')
        match opcion:
            case '1':
               register()
               
            case '2':
                login()
                while (states['is_auth']):
                    role=verificar_rol()
                    match role:
                        case 'admin':
                            mostrar_opciones_para_admin()
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
                            
                        case 'estandar':
                            mostrar_opciones_para_estandar()
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
                
            case _:
                print("la opcion ingresada no es correcta")

        
       

if __name__ == "__main__":
    main()

