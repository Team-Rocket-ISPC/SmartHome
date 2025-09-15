
class UsuarioVivienda:
    ROLES_VALIDOS = {"Admin", "Estandar"}

    def __init__(self, usuario, vivienda_id, rol):
        self.usuario = usuario
        self.vivienda_id = vivienda_id
        self.rol = rol

    # Getter y Setter de usuario
    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Debe ser string")
        self._usuario = value

    # Getter y Setter de nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if "@" not in value or "." not in value:
            raise ValueError("correo debe tener formato válido")
        if not value or len(value.strip()) < 3 :
            raise ValueError("El nombre no puede ser menor a 3 caracteres")
        if len(value) > 50:
            raise ValueError("El nombre no puede superar los 50 caracteres")
        if value not in self.ROLES_VALIDOS:
            raise ValueError(f"rol debe ser uno de {self.ROLES_VALIDOS}")
        self._nombre = value.strip()

    # Getter y Setter de id_vivienda
    @property
    def id_vivienda(self):
        return self._id_vivienda

    @id_vivienda.setter
    def id_vivienda(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Debe ser entero")
        self._id_vivienda = value