from abc import ABC, abstractmethod
from domain.entities.usuario_vivienda import UsuarioVivienda

class IDataAccessUsuarioViviendaDAO(ABC):
    """Interfaz para las operaciones CRUD de UsuarioVivienda en la base de datos."""
    @abstractmethod
    def create(self, usuario_vivienda : UsuarioVivienda) -> bool:
        pass
    @abstractmethod
    def get(self, id) -> UsuarioVivienda:
        pass
    @abstractmethod
    def update(self, id, usuario_vivienda : UsuarioVivienda) -> bool:
        pass
    @abstractmethod
    def delete(self, id) -> bool:
        pass