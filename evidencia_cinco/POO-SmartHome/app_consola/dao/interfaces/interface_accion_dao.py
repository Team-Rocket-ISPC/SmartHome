from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.accion import Accion

class IDataAccesAccionDAO(ABC):
    """Interfaz para el acceso a datos de acciones."""
    @abstractmethod
    def create(self, accion: Accion) -> bool: 
        pass
    @abstractmethod
    def get_all(self) -> List[Accion]:
        pass
    @abstractmethod
    def get_by_tipo(self, id_tipo: int) -> List[Accion]:
        pass
    @abstractmethod
    def get_by_id(self, id_accion: int) -> Optional[Accion]:
        pass
    @abstractmethod
    def update(self, accion: Accion) -> bool:
        pass
    @abstractmethod
    def delete(self, id_accion: int) -> bool:
        pass
