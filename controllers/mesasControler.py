from model.mesas import Mesas
from repositorios.repositorioMesa import RepositorioMesa


class AdministracionMesas():
    def __init__(self):
        self._controlador_mesa = RepositorioMesa()
    
    def mostrar_mesas (self):
        datos_mesa= self._controlador_mesa.findAll()
        return datos_mesa
    
    
    def crear_mesa (self,datos_entrada):
        _mesa = Mesas(datos_entrada)
        return self._controlador_mesa.save(_mesa)
        
    def actualizar_mesa (self,id,datos_entrada):
        _mesa_db =self._controlador_mesa.findById(id)
        _mesa_obj = Mesas (_mesa_db)
        _mesa_obj.codigo = datos_entrada["codigo"]
        _mesa_obj.mesa = datos_entrada["mesa"]
        _mesa_obj.puestovotacion = datos_entrada["puestovotacion"]
        return self._controlador_mesa.save(_mesa_obj)
        
    def eliminar_mesa (self,id):
        return self._controlador_mesa.delete(id)