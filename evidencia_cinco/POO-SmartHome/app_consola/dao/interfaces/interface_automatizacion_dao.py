from abc import ABC, abstractmethod
from domain.entities.automatizacion import Automatizacion

class IDataAccessAutomatizacionDAO(ABC):
    """Interfaz para el acceso a datos de automatizaciones."""
    @abstractmethod
    def create(self, automatizacion: Automatizacion) -> bool:
        """Inserta una nueva automatización en la base de datos."""
        pass

    @abstractmethod
    def get(self, id_automatizacion: int) -> Automatizacion | None:
        """Obtiene una automatización por su ID."""
        pass

    @abstractmethod
    def get_all(self, id_vivienda: int) -> list[Automatizacion]:
        """Obtiene todas las automatizaciones almacenadas."""
        pass

    @abstractmethod
    def update(self, automatizacion: Automatizacion) -> bool:
        """Actualiza los datos de una automatización existente."""
        pass

    @abstractmethod
    def delete(self, id_automatizacion: int) -> bool:
        """Elimina una automatización por su ID."""
        pass

