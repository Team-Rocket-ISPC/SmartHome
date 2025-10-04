class Usuario:
    def __init__(self, correo: str, nombres: str, apellidos: str, contraseña: str, es_activo: bool = True, id: int = None):
        self.correo = correo
        self.nombres = nombres
        self.apellidos = apellidos
        self.contraseña = contraseña
        self.es_activo = es_activo
    
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Correo inválido")
        self._correo = value

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, value):
        if not value or len(value) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        self._nombres = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        if not value or len(value) < 3:
            raise ValueError("El apellido debe tener al menos 3 caracteres")
        self._apellidos = value

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, value):
        if not value or len(value) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        self._contraseña = value

    @property
    def es_activo(self):
        return self._es_activo

    @es_activo.setter
    def es_activo(self, value):
        self._es_activo = value