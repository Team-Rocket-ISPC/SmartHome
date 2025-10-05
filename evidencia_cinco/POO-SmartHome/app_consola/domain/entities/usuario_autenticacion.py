import re
from domain.entities.usuario import Usuario


class UsuarioAutenticacion(Usuario):
    """Clase que representa la autenticación de un usuario en el sistema."""
    def __init__(self, correo: str, nombres: str, apellidos: str, contrasena: str, es_activo: bool, is_auth: bool, role: str):
        self.correo = correo
        self.nombres = nombres
        self.apellidos = apellidos
        self.contrasena = contrasena
        self.es_activo = es_activo
        self.is_auth = is_auth
        self.role = role

    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
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
    
    @property
    def es_activo(self):
        return self._es_activo
    @es_activo.setter
    def es_activo(self, value):
        self._es_activo = value

    @property
    def is_auth(self):
        return self._is_auth
    @is_auth.setter
    def is_auth(self, value):
        self._is_auth = value

    @property
    def role(self):
        return self._role
    @role.setter
    def role(self, value):
        self._role = value
