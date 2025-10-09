from abc import ABC, abstractmethod
from domain.entities.dispositivo import Dispositivo
class IDataAccessDispositivoDAO(ABC):
    @abstractmethod
    def get_by_id(self, id_dispositivo: int) -> Dispositivo:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass
