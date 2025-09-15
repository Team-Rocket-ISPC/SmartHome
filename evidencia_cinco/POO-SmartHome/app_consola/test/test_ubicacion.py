# -------------------------
# TESTS UBICACION
# -------------------------
import pytest
from domain.entities.ubicacion import Ubicacion

def test_crear_ubicacion_valida():
    ubi = Ubicacion(1, "Living", 10)
    assert ubi.id_ubicacion == 1
    assert ubi.nombre == "Living"
    assert ubi.id_vivienda == 10

def test_nombre_vacio():
    with pytest.raises(ValueError):
        Ubicacion(1, "", 10)

def test_nombre_muy_largo():
    with pytest.raises(ValueError):
        Ubicacion(1, "x" * 51, 10)

def test_id_negativo():
    with pytest.raises(ValueError):
        Ubicacion(-1, "Cocina", 5)
