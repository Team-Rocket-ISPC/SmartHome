import pytest
from domain.entities.usuario_vivienda import UsuarioVivienda

def test_crear_usuario_vivienda_valido():
    uv = UsuarioVivienda("user@test.com", 1, "Admin")
    assert uv.correo == "user@test.com"
    assert uv.id_vivienda == 1
    assert uv.rol == "Admin"

def test_correo_invalido():
    with pytest.raises(ValueError):
        UsuarioVivienda("usuario_sin_arroba", 1, "Admin")

def test_rol_invalido():
    with pytest.raises(ValueError):
        UsuarioVivienda("user@test.com", 1, "SuperUser")

def test_id_vivienda_negativo():
    with pytest.raises(ValueError):
        UsuarioVivienda("user@test.com", -2, "Estandar")
