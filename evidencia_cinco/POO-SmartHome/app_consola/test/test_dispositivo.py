import pytest
from domain.entities.dispositivo import Dispositivo

# Clase dummy que simula la Ubicacion
class DummyUbicacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []

# Clase dummy que simula TipoDispositivo
class DummyTipoDispositivo:
    def __init__(self):
        self.id_tipo = 1

@pytest.fixture
def ubicacion():
    return DummyUbicacion("Cocina")

@pytest.fixture
def tipo_dispositivo():
    return DummyTipoDispositivo()

def test_agregar_dispositivo(ubicacion, tipo_dispositivo):
    disp = Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)
    assert disp.nombre == "Luz Cocina"
    assert disp.id_tipo == tipo_dispositivo.id_tipo
    assert disp.ubicacion == ubicacion
    assert disp in ubicacion.dispositivos

def test_eliminar_dispositivo(ubicacion, tipo_dispositivo):
    disp = Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)
    disp.eliminar_dispositivo()
    assert disp not in ubicacion.dispositivos

def test_modificar_dispositivo(ubicacion, tipo_dispositivo):
    disp = Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)
    disp.modificar_dispositivo("Luz Comedor")
    assert disp.nombre == "Luz Comedor"

def test_encender_apagar(ubicacion, tipo_dispositivo):
    disp = Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)
    estado_inicial = disp.estado
    disp.encender_apagar()
    assert disp.estado != estado_inicial
    disp.encender_apagar()
    assert disp.estado == estado_inicial
