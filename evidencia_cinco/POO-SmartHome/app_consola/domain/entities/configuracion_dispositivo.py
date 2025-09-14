class ConfiguracionDispositivo:
    def __init__(self, id_configuracion: int, id_dispositivo: int, atributo: str, valor: str):
        self.id_configuracion = id_configuracion
        self.id_dispositivo = id_dispositivo
        self.atributo = atributo
        self.valor = valor

    # id_configuracion
    @property
    def id_configuracion(self):
        return self._id_configuracion

    @id_configuracion.setter
    def id_configuracion(self, value):
        if not isinstance(value, int):
            raise TypeError("id_configuracion debe ser un número entero")
        if value <= 0:
            raise ValueError("id_configuracion debe ser un entero positivo")
        self._id_configuracion = value

    # id_dispositivo
    @property
    def id_dispositivo(self):
        return self._id_dispositivo

    @id_dispositivo.setter
    def id_dispositivo(self, value):
        if not isinstance(value, int):
            raise TypeError("id_dispositivo debe ser un número entero")
        if value <= 0:
            raise ValueError("id_dispositivo debe ser un entero positivo")
        self._id_dispositivo = value

    # atributo
    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, value):
        if not isinstance(value, str):
            raise TypeError("atributo debe ser un string")
        if not value.strip():
            raise ValueError("atributo no puede estar vacío")
        if len(value) > 50:
            raise ValueError("atributo no puede tener más de 50 caracteres")
        self._atributo = value.strip()

    # valor
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        if not isinstance(value, str):
            raise TypeError("valor debe ser un string")
        if not value.strip():
            raise ValueError("valor no puede estar vacío")
        if len(value) > 50:
            raise ValueError("valor no puede tener más de 50 caracteres")
        self._valor = value.strip()

    def __repr__(self):
        return (f"ConfiguracionDispositivo("
                f"id_configuracion={self.id_configuracion}, "
                f"id_dispositivo={self.id_dispositivo}, "
                f"atributo='{self.atributo}', "
                f"valor='{self.valor}')")
