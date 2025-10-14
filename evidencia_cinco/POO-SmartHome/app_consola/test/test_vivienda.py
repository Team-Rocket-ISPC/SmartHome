import pytest
from domain.entities.vivienda import Vivienda  

def test_crear_vivienda():
    v = Vivienda("Calle 123", 5000, 1)
    assert v.id_vivienda == 1
    assert v.direccion == "Calle 123"
    assert v.codigo_postal == 5000

def test_validacion_direccion_vacia():
    with pytest.raises(ValueError):
        v = Vivienda("", 5000, 1) # Dirección no puede estar vacía

def test_validacion_codigo_postal_incorrecto():
    with pytest.raises(ValueError):
        v = Vivienda("Calle 123", -5000, 1)  # Código postal no puede ser negativo

def test_modificar_vivienda():
    v = Vivienda("Calle 123", 5000, 1)
    v.direccion = "Avenida Illia 742"
    v.codigo_postal = 1000
    v.id_vivienda = 2   
    assert v.direccion == "Avenida Illia 742"
    assert v.codigo_postal == 1000
    assert v.id_vivienda == 2

