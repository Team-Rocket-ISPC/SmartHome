from abc import ABC, abstractmethod
from domain.entities.vivienda import Vivienda

# Interfaces DAO (abstracciones), en dominio

# Interfaz DAO para la entidad Vivienda
class IViviendaDao(ABC):

    @abstractmethod
    def agregar_vivienda(self, vivienda: Vivienda):
        pass

    @abstractmethod
    def obtener_vivienda(self, vivienda_id: int) -> Vivienda:
        pass

    @abstractmethod
    def eliminar_vivienda(self, vivienda_id: int):
        pass

    @abstractmethod
    def listar_viviendas(self) -> list[Vivienda]:
        pass
