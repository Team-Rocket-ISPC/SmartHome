import pytest
from datetime import datetime
from domain.entities.dispositivo import Dispositivo

# ------------------------------
# Tests para nombre
def test_nombre_valido():
    d = Dispositivo("Luz Living", True, datetime(2025, 10, 14, 10, 0))
    assert d.nombre == "Luz Living"

def test_nombre_invalido_corto():
    with pytest.raises(ValueError):
        Dispositivo("A", True, datetime(2025, 10, 14, 10, 0))

def test_nombre_invalido_tipo():
    with pytest.raises(ValueError):
        Dispositivo(123, True, datetime(2025, 10, 14, 10, 0))

# ------------------------------
# Tests para estado
def test_estado_valido_true():
    d = Dispositivo("Luz", True, datetime(2025, 10, 14, 10, 0))
    assert d.estado is True

def test_estado_valido_false():
    d = Dispositivo("Luz", False, datetime(2025, 10, 14, 10, 0))
    assert d.estado is False

def test_estado_invalido_tipo():
    with pytest.raises(ValueError):
        Dispositivo("Luz", "on", datetime(2025, 10, 14, 10, 0))

# ------------------------------
# Tests para fecha_hora
def test_fecha_hora_valida():
    dt = datetime(2025, 10, 14, 10, 0)
    d = Dispositivo("Luz", True, dt)
    assert d.fecha_hora == dt

def test_fecha_hora_invalida_tipo_str():
    with pytest.raises(ValueError):
        Dispositivo("Luz", True, "2025-10-14 10:00")

def test_fecha_hora_invalida_tipo_int():
    with pytest.raises(ValueError):
        Dispositivo("Luz", True, 123456)
