from abc import ABC, abstractmethod
from domain.entities.automatizacion_objetivo import AutomatizacionObjetivo

class IDataAccessAutomatizacionObjetivoDAO(ABC):
    """Interfaz DAO para gestionar los objetivos de las automatizaciones."""
    
    @abstractmethod
    def create(self, objetivo: AutomatizacionObjetivo) -> bool:
        """Agrega un nuevo objetivo a una automatización."""
        pass

    @abstractmethod
    def get_all(self) -> list[AutomatizacionObjetivo]:
        """Obtiene todos los objetivos de automatización."""
        pass

    @abstractmethod
    def get(self, id_automatizacion: int) -> list[AutomatizacionObjetivo]:
        """Obtiene todos los objetivos asociados a una automatización específica."""
        pass

    @abstractmethod
    def delete(self, id_automatizacion: int, id_tipo: int, id_ubicacion: int) -> bool:
        """Elimina un objetivo de una automatización."""
        pass