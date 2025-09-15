from domain.entities.dispositivo import Dispositivo
from domain.entities.ubicacion import Ubicacion 
from domain.entities.tipo_dispositivo import TipoDispositivo 

class AutomatizacionObjetivo:
    def __init__(self, automatizacion, tipo_dispositivo, ubicacion):
        self.automatizacion = automatizacion
        self.tipo_dispositivo = tipo_dispositivo
        self.ubicacion = ubicacion
        automatizacion.objetivos.append(self)

    def aplicar_en(self): #Se invoca en automatizacion.py
        print(f"Aplicando automatización '{self.automatizacion.nombre}' en {self.ubicacion.nombre}")
        for dispositivo in self.ubicacion.dispositivos:
            if dispositivo.id_tipo == self.tipo_dispositivo.id_tipo:
                dispositivo.encender_apagar()
