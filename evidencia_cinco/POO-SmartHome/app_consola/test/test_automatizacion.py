import pytest
from domain.entities.automatizacion import Automatizacion 


def test_nombre_valido():
    auto = Automatizacion("Luz dormitorio", 1, "08:00", "10:00")
    assert auto.nombre == "Luz dormitorio"


def test_nombre_invalido_corto():
    with pytest.raises(ValueError):
        Automatizacion("AB", 1, "08:00", "10:00")


def test_id_vivienda_valido():
    auto = Automatizacion("Luces", 2, "07:00", "09:00")
    assert auto.id_vivienda == 2


def test_id_vivienda_negativo():
    with pytest.raises(ValueError):
        Automatizacion("Luces", -1, "07:00", "09:00")


def test_id_vivienda_no_entero():
    with pytest.raises(TypeError):
        Automatizacion("Luces", "1", "07:00", "09:00")


def test_hora_inicio_valida():
    auto = Automatizacion("Luces", 1, "00:00", "23:59")
    assert auto.hora_inicio == "00:00"


def test_hora_inicio_invalida_formato():
    with pytest.raises(ValueError):
        Automatizacion("Luces", 1, "8:30", "23:59")


def test_hora_inicio_invalida_fuera_rango():
    with pytest.raises(ValueError):
        Automatizacion("Luces", 1, "24:00", "23:59")


def test_hora_fin_valida():
    auto = Automatizacion("Luces", 1, "08:00", "09:00")
    assert auto.hora_fin == "09:00"


def test_hora_fin_invalida_formato():
    with pytest.raises(ValueError):
        Automatizacion("Luces", 1, "08:00", "9-00")


def test_activa_booleana_valida():
    auto = Automatizacion("Luces", 1, "08:00", "09:00", activa=True)
    assert auto.activa is True


def test_activa_invalida_tipo():
    with pytest.raises(ValueError):
        Automatizacion("Luces", 1, "08:00", "09:00", activa="True")

