from abc import ABC, abstractmethod
from domain.entities.usuario import Usuario

class IDataAccessUsuarioDAO(ABC):
    """Interfaz para las operaciones CRUD de Usuario en la base de datos."""
    @abstractmethod
    def get(self, correo: str, contrasena: str) -> Usuario:
        pass
    @abstractmethod
    def get_all(self) -> list[Usuario]:
        pass
    @abstractmethod
    def create(self, usuario: Usuario) -> bool:
        pass
    @abstractmethod
    def update(self, usuario: Usuario) -> bool:
        pass
    @abstractmethod
    def delete(self, correo: str) -> bool:
        pass
    
