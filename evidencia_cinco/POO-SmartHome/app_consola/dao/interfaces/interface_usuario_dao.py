from abc import ABC, abstractmethod

class IDataAccessUsuarioDAO(ABC):
    @abstractmethod
    def get(self, correo: str):
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
