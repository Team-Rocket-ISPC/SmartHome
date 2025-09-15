import pytest
from domain.entities.configuracion_dispositivo import ConfiguracionDispositivo

def test_creacion_correcta():
    config = ConfiguracionDispositivo(1, 10, "modo", "automatico")
    assert config.id_configuracion == 1
    assert config.id_dispositivo == 10
    assert config.atributo == "modo"
    assert config.valor == "automatico"

def test_id_configuracion_invalido():
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(0, 10, "modo", "manual")
    with pytest.raises(TypeError):
        ConfiguracionDispositivo("A", 10, "modo", "manual")

def test_id_dispositivo_invalido():
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(1, -5, "modo", "manual")
    with pytest.raises(TypeError):
        ConfiguracionDispositivo(1, "X", "modo", "manual")

def test_atributo_invalido():
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(1, 10, "", "manual")
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(1, 10, "a" * 51, "manual")
    with pytest.raises(TypeError):
        ConfiguracionDispositivo(1, 10, 123, "manual")

def test_valor_invalido():
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(1, 10, "modo", "")
    with pytest.raises(ValueError):
        ConfiguracionDispositivo(1, 10, "modo", "a" * 51)
    with pytest.raises(TypeError):
        ConfiguracionDispositivo(1, 10, "modo", 123)
    