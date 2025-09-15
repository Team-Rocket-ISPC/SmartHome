class Accion:
    def __init__(self, id_accion: int, nombre: str, id_tipo: int):
        self.id_accion = id_accion
        self.nombre = nombre
        self.id_tipo = id_tipo

    # id_accion
    @property
    def id_accion(self):
        return self._id_accion

    @id_accion.setter
    def id_accion(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El id_accion debe ser un entero positivo.")
        self._id_accion = value

    # nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío.")
        if len(value) > 50:
            raise ValueError("El nombre no puede superar los 50 caracteres.")
        self._nombre = value.strip()

    # id_tipo
    @property
    def id_tipo(self):
        return self._id_tipo

    @id_tipo.setter
    def id_tipo(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El id_tipo debe ser un entero positivo.")
        self._id_tipo = value

