class Usuario:
    def __init__(self, correo: str, nombres: str, apellidos: str, contrasena: str):
        self.correo = correo
        self.nombres = nombres 
        self.apellidos = apellidos
        self.contrasena = contrasena


    def __str__(self):
        return f"Usuario(correo={self.correo}, nombres={self.nombres}, apellidos={self.apellidos})"

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
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, value):
        if not value or len(value) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        self._contrasena = value