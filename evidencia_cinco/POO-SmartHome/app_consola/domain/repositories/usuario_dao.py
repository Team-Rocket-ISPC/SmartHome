from abc import ABC, abstractmethod
from domain.entities.usuario import Usuario

# Interfaces DAO (abstracciones), en dominio

# Interfaz DAO para la entidad Usuario
class IUsuarioDao(ABC):
    # def __init__(self):

    @abstractmethod
    def agregar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_usuario(self, usuario_id: int) -> Usuario:
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario_id: int):
        pass    

    @abstractmethod
    def listar_usuarios(self) -> list[Usuario]:
        pass