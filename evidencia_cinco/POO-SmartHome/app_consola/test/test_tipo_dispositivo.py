import pytest
from tipo_dispositivo import TipoDispositivo

def test_crear_tipo_dispositivo_valido():
    tipo = TipoDispositivo(1, "Sensor")
    assert tipo.id_tipo == 1
    assert tipo.nombre == "Sensor"


def test_tipo_dispositivo_nombre_invalido():
    with pytest.raises(ValueError):
        TipoDispositivo(1, "")


def test_tipo_dispositivo_id_invalido():
    with pytest.raises(ValueError):
        TipoDispositivo(-1, "Sensor")