class TipoDispositivo:
    def __init__(self, id_tipo: int, nombre: str):
        self._id_tipo = None
        self._nombre = None

        self.id_tipo = id_tipo
        self.nombre = nombre

    # Getter y Setter para id_tipo
    @property
    def id_tipo(self):
        return self._id_tipo

    @id_tipo.setter
    def id_tipo(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El id_tipo debe ser un entero positivo.")
        self._id_tipo = value

    # Getter y Setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if len(value) > 50:
            raise ValueError("El nombre no puede superar los 50 caracteres.")
        self._nombre = value
