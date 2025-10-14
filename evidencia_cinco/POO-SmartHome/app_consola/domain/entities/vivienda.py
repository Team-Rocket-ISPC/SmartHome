from typing import Optional

class Vivienda:
    def __init__(self, direccion: str, codigo_postal: int, id_vivienda: Optional[int] = None):
        self.id_vivienda = id_vivienda
        self.direccion = direccion
        self.codigo_postal = codigo_postal

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value: str):
        if not value or len(value.strip()) == 0:
            raise ValueError("La dirección no puede estar vacía o ser solo espacios.")
        self._direccion = value

    @property
    def codigo_postal(self):
        return self._codigo_postal

    @codigo_postal.setter
    def codigo_postal(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El código postal debe ser un número entero positivo.")
        self._codigo_postal = value

    def __str__(self):
         return f"Vivienda ID: {self.id_vivienda}, Dirección: {self.direccion}, Código Postal: {self.codigo_postal}"
