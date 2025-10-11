from abc import ABC, abstractmethod
from domain.entities.vivienda import Vivienda

class IDataAccessViviendaDAO(ABC):

    @abstractmethod
    def get(self, id_vivienda: int) -> Vivienda | None:
        # Obtiene una vivienda por su ID.
        pass

    @abstractmethod
    def get_all(self) -> list[Vivienda]:
        # Obtiene todas las viviendas almacenadas.
        pass

    @abstractmethod
    def create(self, vivienda: Vivienda) -> bool:
        # Inserta una nueva vivienda en la base de datos.
        pass

    @abstractmethod
    def update(self, vivienda: Vivienda) -> bool:
        # Actualiza los datos de una vivienda existente.
        pass

    @abstractmethod
    def delete(self, id_vivienda: int) -> bool:
        # Elimina una vivienda por su ID.
        pass
