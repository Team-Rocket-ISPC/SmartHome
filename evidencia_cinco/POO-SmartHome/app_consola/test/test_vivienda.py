import pytest
from vivienda import Vivienda  

def test_crear_vivienda():
    v = Vivienda(1, "Calle 123", 5000)
    assert v.id_vivienda == 1
    assert v.direccion == "Calle 123"
    assert v.codigo_postal == 5000

def test_modificar_vivienda():
    v = Vivienda(1, "Calle 123", 5000)
    v.modificar_vivienda(direccion="Avenida Illia 742", codigo_postal=10000)
    assert v.direccion == "Avenida Illia 742"
    assert v.codigo_postal == 10000

def test_mostrar_datos_vivienda():
    v = Vivienda(1, "Calle 123", 5000)
    datos = v.mostrar_datos_vivienda()
    assert datos == "Vivienda ID: 1, Dirección: Calle 123, Código Postal: 5000"

def test_validacion_direccion_vacia():
    with pytest.raises(ValueError):
        v = Vivienda(1, "", 5000)

def test_validacion_codigo_postal_incorrecto():
    with pytest.raises(ValueError):
        v = Vivienda(1, "Calle 123", -5000)  # Código postal no puede ser negativo