import pytest
from domain.entities.usuario import Usuario

def test_crear_usuario_valido():
    u = Usuario("correo@test.com", "1234", "Jere")
    assert u.correo == "correo@test.com"
    assert u.nombre == "Jere"

def test_nombre_no_valido():
    with pytest.raises(ValueError):
        Usuario("correo@test.com", "1234", "Je")  # muy corto

def test_correo_no_valido():
    with pytest.raises(ValueError):
        Usuario("correoinvalido", "1234", "jere")  # no tiene @

def test_modificar_usuario_valido():
    u = Usuario("correo@test.com", "1234", "Jere")
    u.nombre = "Jere"
    assert u.nombre == "Jere"

def test_modificar_usuario_invalido():
    u = Usuario("correo@test.com", "1234", "Jere")
    with pytest.raises(ValueError):
        u.correo = "correo_sin_arroba"