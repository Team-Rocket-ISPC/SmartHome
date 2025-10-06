import re
from domain.entities.usuario import Usuario


class UsuarioAutenticacion(Usuario):
    """Clase que representa la autenticación de un usuario en el sistema."""
    def __init__(self, correo, nombres, apellidos, contrasena, es_activo, is_auth: bool, role: str):
        super().__init__(correo, nombres, apellidos, contrasena, es_activo)
        self.is_auth = is_auth
        self.role = role

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
