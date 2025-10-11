from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.ubicacion import Ubicacion

class IDataAccessUbicacionDAO(ABC):

    @abstractmethod
    def get(self, id_ubicacion: int) -> Optional[Ubicacion]:
        """Obtiene una ubicación por su ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[Ubicacion]:
        """Obtiene todas las ubicaciones."""
        pass

    @abstractmethod
    def create(self, ubicacion: Ubicacion) -> bool:
        """Crea una nueva ubicación en la base de datos."""
        pass

    @abstractmethod
    def update(self, ubicacion: Ubicacion) -> bool:
        """Actualiza los datos de una ubicación existente."""
        pass

    @abstractmethod
    def delete(self, id_ubicacion: int) -> bool:
        """Elimina una ubicación de la base de datos."""
        pass
