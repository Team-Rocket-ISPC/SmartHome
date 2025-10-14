from abc import ABC, abstractmethod
from domain.entities.tipo_dispositivo import TipoDispositivo

class IDataAccessTipoDispositivoDAO(ABC):
    """Interfaz para el acceso a datos de TipoDispositivo."""
    @abstractmethod
    def get(self, id_tipo: int) -> TipoDispositivo:
        pass
    @abstractmethod
    def get_all(self) -> list[TipoDispositivo]:
        pass
    @abstractmethod
    def create(self, tipo_dispositivo: TipoDispositivo) -> bool:
        pass
    @abstractmethod
    def update(self, tipo_dispositivo: TipoDispositivo) -> bool:
        pass
    @abstractmethod
    def delete(self, id_tipo: int) -> bool:
        pass