import pytest
from domain.entities.automatizacion import Automatizacion
from domain.entities.tipo_dispositivo import TipoDispositivo
from domain.entities.ubicacion import Ubicacion
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo

# ------------------------------
# objetos válidos
@pytest.fixture
def automatizacion_valida():
    return Automatizacion("Modo Vacaciones", 1, "08:00", "20:00")

@pytest.fixture
def tipo_dispositivo_valido():
    return TipoDispositivo("Luz")

@pytest.fixture
def ubicacion_valida():
    return Ubicacion(id_ubicacion=1, nombre="Living", id_vivienda=1)

# ------------------------------
# Test creación correcta
def test_creacion_correcta(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida):
    ao = AutomatizacionObjetivo(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida)
    assert ao.automatizacion == automatizacion_valida
    assert ao.tipo_dispositivo == tipo_dispositivo_valido
    assert ao.ubicacion == ubicacion_valida

# ------------------------------
# Test errores por tipos inválidos
def test_automatizacion_invalida(tipo_dispositivo_valido, ubicacion_valida):
    with pytest.raises(TypeError):
        AutomatizacionObjetivo("no es automatizacion", tipo_dispositivo_valido, ubicacion_valida)

def test_tipo_dispositivo_invalido(automatizacion_valida, ubicacion_valida):
    with pytest.raises(TypeError):
        AutomatizacionObjetivo(automatizacion_valida, "no es tipo_dispositivo", ubicacion_valida)

def test_ubicacion_invalida(automatizacion_valida, tipo_dispositivo_valido):
    with pytest.raises(TypeError):
        AutomatizacionObjetivo(automatizacion_valida, tipo_dispositivo_valido, "no es ubicacion")

# ------------------------------
# Test setters después de creación
def test_setters_correctos(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida):
    ao = AutomatizacionObjetivo(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida)
    
    # Crear objetos nuevos válidos
    nueva_auto = Automatizacion("Modo Normal", 2, "09:00", "18:00")
    nuevo_disp = TipoDispositivo("Cafetera")
    nueva_ubi = Ubicacion(1, "Cocina", 1)

    ao.automatizacion = nueva_auto
    ao.tipo_dispositivo = nuevo_disp
    ao.ubicacion = nueva_ubi

    assert ao.automatizacion == nueva_auto
    assert ao.tipo_dispositivo == nuevo_disp
    assert ao.ubicacion == nueva_ubi

def test_setters_invalidos(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida):
    ao = AutomatizacionObjetivo(automatizacion_valida, tipo_dispositivo_valido, ubicacion_valida)

    with pytest.raises(TypeError):
        ao.automatizacion = "error"

    with pytest.raises(TypeError):
        ao.tipo_dispositivo = 123

    with pytest.raises(TypeError):
        ao.ubicacion = None

