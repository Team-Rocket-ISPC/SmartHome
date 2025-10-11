from abc import ABC, abstractmethod

class IDataAccessUsuarioDAO(ABC):
    """Interfaz para las operaciones CRUD de Usuario en la base de datos."""
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
    @abstractmethod
    def cambio_rol(self, correo: str, nuevo_rol: str) -> bool:
        pass
