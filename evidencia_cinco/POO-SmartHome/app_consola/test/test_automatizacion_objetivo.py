import pytest
from domain.entities.dispositivo import Dispositivo
from domain.entities.automatizacion import Automatizacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo

# Dummy Ubicacion para los tests
class DummyUbicacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []

# Dummy TipoDispositivo para los tests
class DummyTipoDispositivo:
    def __init__(self, id_tipo):
        self.id_tipo = id_tipo

# Fixtures
@pytest.fixture
def ubicacion():
    return DummyUbicacion("Cocina")

@pytest.fixture
def tipo_dispositivo():
    return DummyTipoDispositivo(1)

@pytest.fixture
def dispositivo(ubicacion, tipo_dispositivo):
    return Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)

@pytest.fixture
def automatizacion():
    return Automatizacion("Modo Vacaciones", "00:00", "23:59")

@pytest.fixture
def objetivo(automatizacion, tipo_dispositivo, ubicacion):
    return AutomatizacionObjetivo(automatizacion, tipo_dispositivo, ubicacion)

# Tests
def test_objetivo_se_agrega_a_automatizacion(objetivo, automatizacion):
    assert objetivo in automatizacion.objetivos

def test_aplicar_en_cambia_estado_dispositivo(objetivo, dispositivo):
    # dispositivo inicial apagado
    assert dispositivo.estado is False
    objetivo.aplicar_en()
    assert dispositivo.estado is True
    # volver a aplicar para apagar
    objetivo.aplicar_en()
    assert dispositivo.estado is False

def test_aplicar_en_no_afecta_dispositivos_diferentes(objetivo, ubicacion):
    # agregamos otro dispositivo de tipo distinto
    tipo_otro = DummyTipoDispositivo(2)
    disp_otro = Dispositivo.agregar_dispositivo("Aire Acondicionado", tipo_otro, ubicacion)
    # aplicar objetivo
    objetivo.aplicar_en()
    # el dispositivo de tipo diferente no debe cambiar
    assert disp_otro.estado is False
