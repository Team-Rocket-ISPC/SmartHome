class Usuario:
    def __init__(self, correo: str, contraseña: str, nombre: str):
        self.correo = correo
        self.contraseña = contraseña
        self.nombre = nombre

    
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Correo inválido")
        self._correo = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or len(value) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        self._nombre = value

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, value):
        if not value or len(value) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        self._contraseña = value