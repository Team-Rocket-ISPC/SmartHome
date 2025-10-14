from datetime import datetime


class Dispositivo:
    def __init__(self, nombre, estado, fecha_hora, id_tipo = None, id_ubicacion = None, id_dispositivo = None):
        self.nombre = nombre
        self.estado = estado
        self.fecha_hora = fecha_hora
        self.id_tipo = id_tipo
        self.id_ubicacion = id_ubicacion
        self.id_dispositivo = id_dispositivo
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser un texto.")
        if len(valor.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado debe ser booleano (True o False).")
        self._estado = valor

    @property
    def fecha_hora(self):
        return self._fecha_hora

    @fecha_hora.setter
    def fecha_hora(self, valor):
        if not isinstance(valor, datetime):
            raise ValueError("La fecha y hora deben ser un objeto datetime.")
        self._fecha_hora = valor

#-----------------------------------------------------------------------------------------------------------#

    def __str__(self):
        return f"Dispositivo: nombre={self.nombre}, estado={self.estado}, fecha_hora={self.fecha_hora}, tipo={self.id_tipo}, ubicacion={self.id_ubicacion}, id_dispositivo={self.id_dispositivo}"

    def encender_apagar(self):
        self.estado = not self.estado
        estado_txt = "ENCENDIDO" if self.estado else "APAGADO"
        print(f"{self.nombre} ahora está {estado_txt}")
        # Actualiza en base de datos
        from dao.dispositivo_dao import DispositivoDAO
        dispositivo_dao = DispositivoDAO()
        dispositivo_dao.update_estado(self.id_dispositivo, self.estado)


