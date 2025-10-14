from abc import ABC, abstractmethod
from domain.entities.usuario_vivienda import UsuarioVivienda

class IDataAccessUsuarioViviendaDAO(ABC):
    """Interfaz para las operaciones CRUD de UsuarioVivienda en la base de datos."""
    @abstractmethod
    def create(self, usuario_vivienda : UsuarioVivienda) -> bool:
        pass
    @abstractmethod
    def get(self, correo: str) -> UsuarioVivienda:
        pass
    @abstractmethod
    def update(self, correo: str, usuario_vivienda: UsuarioVivienda) -> bool:
        pass
    @abstractmethod
    def delete(self, correo: str) -> bool:
        pass
    @abstractmethod
    def cambio_rol(self, correo: str, nuevo_rol: str) -> bool:
        pass