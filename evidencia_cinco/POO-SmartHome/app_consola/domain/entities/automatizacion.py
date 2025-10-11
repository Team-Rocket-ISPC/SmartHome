from datetime import datetime


class Automatizacion:
    def __init__(self, nombre, id_vivienda, hora_inicio, hora_fin, activa=False, id_automatizacion=None):
        self.id_automatizacion = id_automatizacion  # Se asigna en la BD. Puede ser None al crear una nueva automatización
        self.nombre = nombre
        self.id_vivienda = id_vivienda
        self.hora_inicio = hora_inicio  # formato "HH:MM"
        self.hora_fin = hora_fin        # formato "HH:MM"
        self.activa = activa
        self.objetivos = []  # composición: se insertan desde lista de automatizacion_objetivo

    def __str__(self):
        return f"Automatización(ID={self.id_automatizacion}, nombre={self.nombre}, id_vivienda={self.id_vivienda}, " \
               f"hora_inicio={self.hora_inicio}, hora_fin={self.hora_fin}, activa={self.activa})"
    
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




    