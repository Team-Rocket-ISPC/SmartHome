from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.dispositivo import Dispositivo

class IDataAccessDispositivoDAO(ABC):
    """Interfaz para operaciones CRUD de Dispositivo."""
    @abstractmethod
    def create(self, dispositivo: Dispositivo) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Dispositivo]:
        pass

    @abstractmethod
    def get_by_id(self, id_dispositivo: int) -> Optional[Dispositivo]:
        pass

    @abstractmethod
    def update(self, dispositivo: Dispositivo) -> bool:
        pass
    
    @abstractmethod
    def update_estado(self, id_dispositivo: int, nuevo_estado: bool) -> bool:
        pass

    @abstractmethod
    def delete(self, id_dispositivo: int) -> bool:
        pass
