from abc import ABC, abstractmethod

class IDataAccesaccionDAO(ABC):
    @abstractmethod
    def get(self, id_acccion: int):
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
