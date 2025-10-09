from abc import ABC, abstractmethod
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo

class IDataAccessAutomatizacionObjetivoDAO(ABC):

    @abstractmethod
    def create(self, objetivo: AutomatizacionObjetivo) -> bool:
        pass

    @abstractmethod
    def get(self, id_automatizacion: int) -> list[AutomatizacionObjetivo]:
        pass

    @abstractmethod
    def get_all(self) -> list[AutomatizacionObjetivo]:
        pass


    @abstractmethod
    def delete(self, id_automatizacion: int, id_tipo: int, id_ubicacion: int) -> bool:
        pass