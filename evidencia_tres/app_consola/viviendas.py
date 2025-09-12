from base_de_datos import base_de_datos


def crear_vivienda(direccion, id_usuario):
    nueva = {
        "id_vivienda": len(base_de_datos['viviendas']) + 1,
        "direccion": direccion,
        "id_usuario": id_usuario
    }
    base_de_datos['viviendas'].append(nueva)
    print("Vivienda agregada con exito.")

def mostrar_viviendas():
    for v in base_de_datos['viviendas']:
        print(v)

def buscar_viviendas_por_usuario(id_usuario):
    for v in base_de_datos['viviendas']:
        if v["id_usuario"] == id_usuario:
            print(v)
