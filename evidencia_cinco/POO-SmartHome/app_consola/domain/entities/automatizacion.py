from datetime import datetime
from automatizacion_objetivo import AutomatizacionObjetivo

class Automatizacion:
    ultimo_id = 0  # atributo de clase para autoincremento

    def __init__(self, nombre, hora_inicio, hora_fin):
        Automatizacion.ultimo_id += 1   # autoincrementar el ID al crear la automatización
        self.id_automatizacion = Automatizacion.ultimo_id
        self.nombre = nombre
        self.hora_inicio = hora_inicio  # formato "HH:MM"
        self.hora_fin = hora_fin        # formato "HH:MM"
        self.activa = False
        self.objetivos = []  # composición: lista de AutomatizacionObjetivo

    def activar(self):
        self.activa = True
        print(f"Automatización '{self.nombre}' ACTIVADA")

    def desactivar(self):
        self.activa = False
        print(f"Automatización '{self.nombre}' DESACTIVADA")

    def esta_en_horario(self): #Verifica si la hora actual está dentro del rango de la automatización
        ahora = datetime.now().time()
        h_inicio = datetime.strptime(self.hora_inicio, "%H:%M").time()
        h_fin = datetime.strptime(self.hora_fin, "%H:%M").time()

        if h_inicio < h_fin:
            # Caso normal (ej: 08:00 a 20:00)
            return h_inicio <= ahora <= h_fin
        else:
            # Caso pasa medianoche (ej: 22:00 a 06:00)
            return ahora >= h_inicio or ahora <= h_fin

    def ejecutar(self):
        if not self.activa:
            print(f"Automatización '{self.nombre}' está inactiva")
            return

        if not self.esta_en_horario():
            print(f"No es horario de la automatización '{self.nombre}'")
            return

        print(f"Ejecutando automatización '{self.nombre}'")
        for obj in self.objetivos:
            obj.aplicar_en()




    