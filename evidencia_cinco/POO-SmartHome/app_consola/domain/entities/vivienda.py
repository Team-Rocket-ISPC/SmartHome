

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

    def crear_vivienda(self, direccion: str, codigo_postal: int):
        """Crea una nueva vivienda (sin id_vivienda, ya que se asignará automáticamente)."""
        self.direccion = direccion
        self.codigo_postal = codigo_postal

    def modificar_vivienda(self, direccion: str = None, codigo_postal: int = None):
        """Modifica los atributos de la vivienda, si los valores son proporcionados."""
        if direccion:
            self.direccion = direccion
        if codigo_postal:
            self.codigo_postal = codigo_postal

    def mostrar_datos_vivienda(self):
        """Devuelve una cadena con los detalles de la vivienda."""
        return f"Vivienda ID: {self.id_vivienda}, Dirección: {self.direccion}, Código Postal: {self.codigo_postal}"
