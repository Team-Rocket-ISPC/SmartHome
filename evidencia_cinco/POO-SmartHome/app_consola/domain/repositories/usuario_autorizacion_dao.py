
from abc import ABC, abstractmethod
from domain.entities.usuario_autenticacion import UsuarioAutenticacion

# Interfaz DAO para la entidad UsuarioAutenticacion
class IUsuarioAutorizacionDao(ABC):
    @abstractmethod
    def autorizar_usuario(self, correo: str, contrasena: str) -> UsuarioAutenticacion:
        pass

