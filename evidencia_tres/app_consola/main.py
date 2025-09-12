from menu import llamar_opciones_para_admin, llamar_opciones_para_estandar, mostrar_opciones_principal_de_app, mostrar_opciones_para_admin, mostrar_opciones_para_estandar 
from automatizaciones import iniciar_automatizacion_aspiradora, iniciar_automatizacion_luces_del_patio
import datetime
from auth import verificar_rol, login, register
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
                            llamar_opciones_para_admin()
                            
                        case 'estandar':
                            mostrar_opciones_para_estandar()
                            llamar_opciones_para_estandar()
            case '3':
                print("Hasta la proxima.")
                break
            case _:
                print("la opcion ingresada no es correcta")

        
       

if __name__ == "__main__":
    main()

