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
    
    @property
    def nombre(self):
        return self._nombres

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        self._nombre = value

    @property
    def id_vivienda(self):
        return self._id_vivienda

    @id_vivienda.setter
    def id_vivienda(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Debe ser entero")
        elif value < 0:
            raise ValueError("El id de la vivienda no puede ser negativo")
        self._id_vivienda = value

    @property
    def hora_inicio(self):
        return self._hora_inicio    

    @hora_inicio.setter
    def hora_inicio(self, valor):
        if not isinstance(valor, str) or len(valor.split(":")) != 2: #esto verifica que haya 2 terminos separados por ":"
            raise ValueError("La hora de inicio debe estar en formato 'HH:MM'")
        horas, minutos = valor.split(":")
        if not (horas.isdigit() and minutos.isdigit()): #esto verifica que ambos terminos sean numeros str
            raise ValueError("La hora de inicio debe contener solo números y ':'")
        horas, minutos = int(horas), int(minutos)
        if not (0 <= horas <= 23 and 0 <= minutos <= 59): 
            raise ValueError("La hora de inicio debe estar entre 00:00 y 23:59")
        self._hora_inicio = valor

    @property
    def hora_fin(self):
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, valor):
        if not isinstance(valor, str) or len(valor.split(":")) != 2:
            raise ValueError("La hora de fin debe estar en formato 'HH:MM'")
        horas, minutos = valor.split(":")
        if not (horas.isdigit() and minutos.isdigit()):
            raise ValueError("La hora de fin debe contener solo números y ':'")
        horas, minutos = int(horas), int(minutos)
        if not (0 <= horas <= 23 and 0 <= minutos <= 59):
            raise ValueError("La hora de fin debe estar entre 00:00 y 23:59")
        self._hora_fin = valor

    @property
    def activa(self):
        return self._activa

    @activa.setter
    def activa(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El atributo 'activa' debe ser True o False.")
        self._activa = valor
        
#-----------------------------------------------------------------------------------------#    
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




    