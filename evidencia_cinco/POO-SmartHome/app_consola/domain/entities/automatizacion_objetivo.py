from domain.entities.dispositivo import Dispositivo
from domain.entities.ubicacion import Ubicacion 
from domain.entities.tipo_dispositivo import TipoDispositivo 

class AutomatizacionObjetivo:
    def __init__(self, automatizacion, tipo_dispositivo, ubicacion):
        self.automatizacion = automatizacion
        self.tipo_dispositivo = tipo_dispositivo
        self.ubicacion = ubicacion
        automatizacion.objetivos.append(self) 
    #estos objetivos hay que pedirlos por consola haciendo un get por id vivienda a tipo y ubicacion 

    def __str__(self):
        return f"Tipo: {self.tipo_dispositivo.nombre}, Ubicación: {self.ubicacion.nombre}"    
  
    def aplicar_en(self): #Se invoca en automatizacion.py
        print(f"Aplicando automatización '{self.automatizacion.nombre}' en {self.ubicacion.nombre}")
        for dispositivo in self.ubicacion.dispositivos:
            if dispositivo.id_tipo == self.tipo_dispositivo.id_tipo:
                dispositivo.encender_apagar()
   
# Ejemplo de uso:
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
