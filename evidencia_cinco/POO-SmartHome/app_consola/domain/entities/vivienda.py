class Vivienda:
    def __init__(self, id_vivienda: int, direccion: str, codigo_postal: str):
        self.id_vivienda = id_vivienda
        self.direccion = direccion 
        self.codigo_postal = codigo_postal 

    @property
    def id_vivienda(self):
        return self._id_vivienda
    @id_vivienda.setter
    def id_vivienda(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID de la vivienda debe ser un entero positivo.")
        self._id_vivienda = value    

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("La dirección no puede estar vacía o ser solo espacios.")
        self._direccion = value

    @property
    def codigo_postal(self):
        return self._codigo_postal

    @codigo_postal.setter
    def codigo_postal(self, value):
        if not value or len(value.strip()) < 4:
            raise ValueError("El código postal no puede tener menos de 4 caracteres.")
        self._codigo_postal = value

    # def crear_vivienda(self, id_vivienda: int, direccion: str, codigo_postal: int):
    #     """Crea o actualiza la vivienda con los datos proporcionados."""
    #     self.id_vivienda = id_vivienda
    #     self.direccion = direccion  
    #     self.codigo_postal = codigo_postal  

    # def modificar_vivienda(self, direccion: str = None, codigo_postal: int = None):
    #     """Modifica los atributos de la vivienda, si los valores son proporcionados."""
    #     if direccion:
    #         self.direccion = direccion  
    #     if codigo_postal:
    #         self.codigo_postal = codigo_postal 

    # def mostrar_datos_vivienda(self):
    #     """Devuelve una cadena con los detalles de la vivienda."""
    #     return f"Vivienda ID: {self.id_vivienda}, Dirección: {self.direccion}, Código Postal: {self.codigo_postal}"