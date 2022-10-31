from model.partidos import Partidos
from repositorios.repositorioPartido import RepositorioPartido



class AdministracionPartidos():
    def __init__(self):
        self._controlador_partido = RepositorioPartido()
    
    def mostrar_partidos (self):
        datos_partido= self._controlador_partido.findAll()
        return datos_partido
    
    
    def crear_partido (self,datos_entrada):
        _partido = Partidos(datos_entrada)
        return self._controlador_partido.save(_partido)
        
    def actualizar_partido (self,id,datos_entrada):
        _partido_db =self._controlador_partido.findById(id)
        _partido_obj = Partidos (_partido_db)
        _partido_obj.codigo = datos_entrada["codigo"]
        _partido_obj.partido = datos_entrada["partido"]
        _partido_obj.tipoDeLista = datos_entrada["tipoDeLista"]
        return self._controlador_partido.save(_partido_obj)
        
    def eliminar_partido (self,id):
        return self._controlador_partido.delete(id)