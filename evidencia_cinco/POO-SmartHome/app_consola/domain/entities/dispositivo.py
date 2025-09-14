#from ubicacion import Ubicacion  #Revisar al finalizar que se hayan nomeclado igual los modulos y clases
#from tipo_dispositivo import TipoDispositivo #Revisar al finalizar que se hayan nomeclado igual los modulos y clases

class Dispositivo:
    ultimo_id = 0  # atributo de clase para autoincremento de id_dispositivo--> Aplicar igual en Vivienda y id_tipo
    
    def __init__(self, id_dispositivo, nombre, id_tipo, ubicacion):
        self.id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.estado = False  # False=OFF, True=ON
        self.id_tipo = id_tipo
        self.ubicacion = ubicacion
        ubicacion.dispositivos.append(self) #EN EL MODULO UBICACION CREAR UNA LISTA dispositivos 
                                            #para agregarlos y poder listarlos con mostrar_dispositivos()

    @staticmethod # No hace falta instanciarlo primero--> Dispositivo.agregar_dipositivo(nombre,tipo,ubicacion)
    def agregar_dispositivo(nombre, tipo_dispositivo, ubicacion): 
        Dispositivo.ultimo_id += 1  # autoincrementar ID --> Aplicar igual en Vivienda y id_tipo
        nuevo = Dispositivo(Dispositivo.ultimo_id, nombre, tipo_dispositivo.id_tipo, ubicacion)
        print(f"Dispositivo agregado: {nuevo.nombre} en {ubicacion.nombre}")
        return nuevo

    def eliminar_dispositivo(self):
        if self in self.ubicacion.dispositivos:
            self.ubicacion.dispositivos.remove(self)
            print(f"Dispositivo {self.nombre} eliminado de {self.ubicacion.nombre}")
        else:
            print(f"El dispositivo {self.nombre} no estaba registrado en {self.ubicacion.nombre}")

    def modificar_dispositivo(self, nuevo_nombre=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        print(f"Dispositivo modificado: {self.nombre}")

    def mostrar_datos_dispositivo(self):
        estado_txt = "ENCENDIDO" if self.estado else "APAGADO"
        print(f"[Dispositivo {self.id_dispositivo}] {self.nombre} - Estado: {estado_txt}")

    def encender_apagar(self):
        self.estado = not self.estado
        estado_txt = "ENCENDIDO" if self.estado else "APAGADO"
        print(f"{self.nombre} ahora está {estado_txt}")


#CONSIDERACIONES BORRAR AL ULTIMO        
# suponiendo que tipo_luz y tipo_aire son instancias de TipoDispositivo

#Dispositivo.agregar_dispositivo("Luz cocina", tipo_luz, cocina)
#Dispositivo.agregar_dispositivo("Aire acondicionado", tipo_aire, living)

#Resultado:
#Dispositivo agregado: Luz cocina en Cocina
#Dispositivo agregado: Aire acondicionado en Living

#Lo puse para que tome tipo_dispositivo.id_tipo --> TipoDispositivo también tiene su propio autoincremento, se maneja igual que en Dispositivo.
#Cuando conectemos con la BD, esto se va a mapear directo a la FK tipo_dispositivo.id_tipo.