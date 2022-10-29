import pymongo
import certifi
import json
from typing import Generic, TypeVar

T = TypeVar("T")

class InterfazRepositorio(Generic[T]):
    def __init__(self):
        datos_conf =self.cargar_configuracion()
        ca =certifi.where()
        client = pymongo.MongoClient(datos_conf["servidor-bd"], tlsCAFile = ca)
        self.db = client[datos_conf["nombre-bd"]]
        
    def consultar_coleccion(self):
        _mesa_coleccion = self.db.mesas
        datos= []
        for mesas in _mesa_coleccion.find():
            mesas["_id"] = str(mesas["_id"])
            datos.append(mesas)
        return datos
        
    def cargar_configuracion(self):
        with open ("config.json") as archivo:
            datos_configuracion = json.load(archivo)
        return datos_configuracion