from model.mesaModelo import AdministracionMesa
from repositorios.repositorioMesa import RepositorioMesa


class AdministracionMesas():
    def __init__(self):
        self._controlador_mesa = RepositorioMesa()
    
    def mostrar_mesas (self):
        datos_mesa= self._controlador_mesa.consultar_coleccion()
        return datos_mesa
    
    
    def crear_mesa (self,datos_entrada):
        _mesa = AdministracionMesas(datos_entrada)
        return _mesa.__dict__
        
        
        
    def actualizar_mesa (self,datos_entrada):
        mesa = AdministracionMesas(datos_entrada)
        return mesa.__dict__
        
    def eliminar_mesa (self,id):
        respuesta = {
            "respuesta": "Mesa con codigo" + id + "eliminado"
        }
        return respuesta