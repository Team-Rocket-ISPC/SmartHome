
class Ubicacion:
    def __init__(self, id_ubicacion: int, nombre: str, id_vivienda: int):
        self.id_ubicacion = id_ubicacion
        self.nombre = nombre
        self.id_vivienda = id_vivienda
         
    # Getter y Setter de id_ubicacion
    @property
    def id_ubicacion(self):
        return self._id_ubicacion


    @id_ubicacion.setter
    def id_ubicacion(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Debe ser entero")
        #se agrega esta validacion para que pase el test si el id es negativo
        elif value < 0:
            raise ValueError("El id de la ubicación no puede ser negativo")
        self._id_ubicacion = value

    # Getter y Setter de nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if not value or len(value.strip()) <3 :
            raise ValueError("El nombre no puede ser menor a 3 caracteres")
        if len(value) > 50:
            raise ValueError("El nombre no puede superar los 50 caracteres")
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

    def __str__(self):
        return f"Id: {self.id_ubicacion}, Nombre: {self.nombre}, Id vivienda: {self.id_vivienda}"
