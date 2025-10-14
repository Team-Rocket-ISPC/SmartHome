import pytest
from domain.entities.usuario import Usuario

def test_crear_usuario_valido():
    u = Usuario("correo@test.com", "nombre", "apellido", "1234")
    assert u.correo == "correo@test.com"
    assert u.nombres == "nombre"
    assert u.apellidos == "apellido"
    assert u.contrasena == "1234"

def test_nombre_no_valido():
    with pytest.raises(ValueError):
        Usuario("correo@test.com", "no", "apellido", "1234")  # muy corto

def test_apellido_no_valido():
    with pytest.raises(ValueError):
        Usuario("correo@test.com", "nombre", "no", "1234")  # muy corto

def test_correo_no_valido():
    with pytest.raises(ValueError):
        Usuario("correoinvalido", "nombre", "apellido", "1234")  # no tiene @

def test_contrasena_no_valida():
    with pytest.raises(ValueError):
        Usuario("correo@test.com", "nombre", "apellido", "1")  # muy corta

def test_modificar_usuario_valido():
    u = Usuario("correo@test.com", "nombre", "apellido", "1234")
    u.nombres = "Otro"
    assert u.nombres == "Otro"

def test_modificar_usuario_invalido():
    u = Usuario("correo@test.com", "nombre", "apellido", "1234")
    with pytest.raises(ValueError):
        u.correo = "correo_sin_arroba"