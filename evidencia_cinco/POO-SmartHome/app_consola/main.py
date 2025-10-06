import datetime
from app.ui import UI

def main():
    # Quiero que al iniciar el sistema me muestre el dia y la hora actual
    ahora = datetime.datetime.now()
    print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        result = UI.ejecutar_menu_principal()
        if result == 'Registro completado':
            print("Registro completado exitosamente.")
        elif result == 'Error en registro':
            print("Hubo un error en el registro. Intente nuevamente.")
        
        if result == 'Salir':
            print("Saliendo del sistema...")
            break


    
if __name__ == "__main__":
    main()
