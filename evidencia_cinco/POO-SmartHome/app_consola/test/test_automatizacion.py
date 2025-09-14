import pytest
from datetime import datetime
from domain.entities.automatizacion import Automatizacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo
from domain.entities.dispositivo import Dispositivo  

# Clases dummy para reemplazar Ubicacion y TipoDispositivo hasta que esten creadas
class DummyUbicacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []

class DummyTipoDispositivo:
    def __init__(self, id_tipo):
        self.id_tipo = id_tipo

@pytest.fixture
def ubicacion():
    return DummyUbicacion("Cocina")

@pytest.fixture
def tipo_dispositivo():
    return DummyTipoDispositivo(1)

@pytest.fixture
def dispositivo(ubicacion, tipo_dispositivo):
    # Usamos la clase real Dispositivo
    return Dispositivo.agregar_dispositivo("Luz Cocina", tipo_dispositivo, ubicacion)

@pytest.fixture
def automatizacion():
    return Automatizacion("Modo Vacaciones", "00:00", "23:59")

def test_activar_desactivar(automatizacion):
    automatizacion.activar()
    assert automatizacion.activa is True
    automatizacion.desactivar()
    assert automatizacion.activa is False

def test_esta_en_horario(automatizacion):
    # Para test rápido usamos horario siempre válido
    assert automatizacion.esta_en_horario() is True

def test_ejecutar_automatizacion_activa(automatizacion, tipo_dispositivo, ubicacion, dispositivo):
    # Creamos un objetivo
    objetivo = AutomatizacionObjetivo(automatizacion, tipo_dispositivo, ubicacion)
    automatizacion.activar()
    # Antes de ejecutar, dispositivo está apagado
    assert dispositivo.estado is False
    automatizacion.ejecutar()
    # Después de ejecutar, se enciende/apaga
    assert dispositivo.estado is True
