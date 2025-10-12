
class UsuarioVivienda:
    """Clase que representa la relación entre un usuario y una vivienda en el sistema SmartHome."""
    ROLES_VALIDOS = {"Admin", "Estandar"}

    def __init__(self, correo, id_vivienda, rol):
        self.correo = correo
        self.id_vivienda = id_vivienda
        self.rol = rol

    # Getter y Setter de correo
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Debe ser string")
        if "@" not in value or "." not in value:
            raise ValueError("El correo debe tener formato válido")
        if not value.strip() or len(value.strip()) < 3:
            raise ValueError("El correo no puede tener menos de 3 caracteres")
        if len(value) > 50:
            raise ValueError("El correo no puede superar los 50 caracteres")
        self._correo = value.strip()
       

    # Getter y Setter de id_vivienda
    @property
    def id_vivienda(self):
        return self._id_vivienda

    @id_vivienda.setter
    def id_vivienda(self, value: int):
        if not isinstance(value, int):
            raise TypeError("El id de la vivienda debe ser un entero")
        if value < 0:
            raise ValueError("El id de la vivienda no puede ser negativo")
        self._id_vivienda = value

    # Getter y Setter de rol
    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, value: str):
        if not isinstance(value, str):
            raise TypeError("El rol debe ser un string")
        if value not in self.ROLES_VALIDOS:
            raise ValueError(f"El rol debe ser uno de {self.ROLES_VALIDOS}")
        self._rol = value