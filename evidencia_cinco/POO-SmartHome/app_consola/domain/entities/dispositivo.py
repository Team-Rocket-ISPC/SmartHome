from datetime import datetime

class Dispositivo:
    def __init__(self, nombre, estado, fecha_hora, id_tipo = None, id_ubicacion = None, id_dispositivo = None):
        self.nombre = nombre
        self.estado = estado
        self.fecha_hora = fecha_hora
        self.id_tipo = id_tipo
        self.id_ubicacion = id_ubicacion
        self.id_dispositivo = id_dispositivo
        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, valor):
            if not isinstance(valor, str):
                raise ValueError("El nombre debe ser un texto.")
            if len(valor.strip()) < 2:
                raise ValueError("El nombre debe tener al menos 2 caracteres.")
            self._nombre = valor.strip()

        @property
        def estado(self):
            return self._estado

        @estado.setter
        def estado(self, valor):
            if not isinstance(valor, bool):
                raise ValueError("El estado debe ser booleano (True o False).")
            self._estado = valor

        @property
        def fecha_hora(self):
            return self._fecha_hora

        @fecha_hora.setter
        def fecha_hora(self, valor):
            if not isinstance(valor, datetime):
                raise ValueError("La fecha y hora deben ser un objeto datetime.")
            self._fecha_hora = valor

    
    def __str__(self):
        return f"Dispositivo(nombre={self.nombre}, estado={self.estado}, fecha_hora={self.fecha_hora}, tipo={self.id_tipo}, ubicacion={self.id_ubicacion}, id_dispositivo={self.id_dispositivo})"

#from domain.entities.tipo_dispositivo import TipoDispositivo #Revisar al finalizar que se hayan nomeclado igual los modulos y clases
#from domain.entities.ubicacion import Ubicacion #Revisar al finalizar que se hayan nomeclado igual los modulos y clases
  
# class Dispositivo:
#     ultimo_id = 0  # atributo de clase para autoincremento de id_dispositivo--> Aplicar igual en Vivienda y id_tipo
    
#     def __init__(self, id_dispositivo, nombre, id_tipo, ubicacion):
#         self.id_dispositivo = id_dispositivo
#         self.nombre = nombre
#         self.estado = False  # False=OFF, True=ON
#         self.id_tipo = id_tipo
#         self.ubicacion = ubicacion
#         ubicacion.dispositivos.append(self) #EN EL MODULO UBICACION CREAR UNA LISTA dispositivos 
#                                             #para agregarlos y poder listarlos con mostrar_dispositivos()

#     @staticmethod # No hace falta instanciarlo primero--> Dispositivo.agregar_dipositivo(nombre,tipo,ubicacion)
#     def agregar_dispositivo(nombre, tipo_dispositivo, ubicacion): 
#         Dispositivo.ultimo_id += 1  # autoincrementar ID --> Aplicar igual en Vivienda y id_tipo
#         nuevo = Dispositivo(Dispositivo.ultimo_id, nombre, tipo_dispositivo.id_tipo, ubicacion)
#         print(f"Dispositivo agregado: {nuevo.nombre} en {ubicacion.nombre}")
#         return nuevo

#     def eliminar_dispositivo(self):
#         if self in self.ubicacion.dispositivos:
#             self.ubicacion.dispositivos.remove(self)
#             print(f"Dispositivo {self.nombre} eliminado de {self.ubicacion.nombre}")
#         else:
#             print(f"El dispositivo {self.nombre} no estaba registrado en {self.ubicacion.nombre}")

#     def modificar_dispositivo(self, nuevo_nombre=None):
#         if nuevo_nombre:
#             self.nombre = nuevo_nombre
#         print(f"Dispositivo modificado: {self.nombre}")

#     def mostrar_datos_dispositivo(self):
#         estado_txt = "ENCENDIDO" if self.estado else "APAGADO"
#         print(f"[Dispositivo {self.id_dispositivo}] {self.nombre} - Estado: {estado_txt}")

#     def encender_apagar(self):
#         self.estado = not self.estado
#         estado_txt = "ENCENDIDO" if self.estado else "APAGADO"
#         print(f"{self.nombre} ahora está {estado_txt}")


#CONSIDERACIONES BORRAR AL ULTIMO        
# suponiendo que tipo_luz y tipo_aire son instancias de TipoDispositivo

#Dispositivo.agregar_dispositivo("Luz cocina", tipo_luz, cocina)
#Dispositivo.agregar_dispositivo("Aire acondicionado", tipo_aire, living)

#Resultado:
#Dispositivo agregado: Luz cocina en Cocina
#Dispositivo agregado: Aire acondicionado en Living

#Lo puse para que tome tipo_dispositivo.id_tipo --> TipoDispositivo también tiene su propio autoincremento, se maneja igual que en Dispositivo.
#Cuando conectemos con la BD, esto se va a mapear directo a la FK tipo_dispositivo.id_tipo.