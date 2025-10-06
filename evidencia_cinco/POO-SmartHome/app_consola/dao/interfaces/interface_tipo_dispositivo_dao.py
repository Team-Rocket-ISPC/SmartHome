from abc import ABC, abstractmethod

class IDataAccessTipoDispositivoDAO(ABC):
    @abstractmethod
    def get(self, id_tipo: int):
        pass
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def create(self, object):
        pass
    @abstractmethod
    def update(self, object ):
        pass
    @abstractmethod
    def delete(self, object):
        pass