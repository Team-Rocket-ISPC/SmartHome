import pytest
from entities import Accion


# ---- TESTS PARA ACCION ----
def test_crear_accion_valida():
    accion = Accion(1, "Encender", 10)
    assert accion.id_accion == 1
    assert accion.nombre == "Encender"
    assert accion.id_tipo == 10


def test_accion_nombre_vacio():
    with pytest.raises(ValueError):
        Accion(2, "", 10)


def test_accion_nombre_largo():
    with pytest.raises(ValueError):
        Accion(3, "x" * 51, 10)


def test_accion_id_invalido():
    with pytest.raises(ValueError):
        Accion(-1, "Apagar", 10)
