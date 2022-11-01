from model.resultados import Resultados
from repositorios.repositorioResultados import RepositorioResultados


class AdministracionResultados():
    def __init__(self):
        self._controlador_resultados = RepositorioResultados()
    
    def mostrar_resultados (self):
        datos_resultados= self._controlador_resultados.findAll()
        return datos_resultados
    
    
    def crear_resultados (self,datos_entrada):
        _resultados = Resultados(datos_entrada)
        return self._controlador_resultados.save(_resultados)
        
    def actualizar_resultados (self,id,datos_entrada):
        _resultados_db                 = self._controlador_resultados.findById(id)
        _resultados_obj                = Resultados (_resultados_db)
        _resultados_obj.codigo         = datos_entrada["codigo"]
        _resultados_obj.resultados     = datos_entrada["resultados"]
        _resultados_obj.puestovotacion = datos_entrada["puestovotacion"]
        return self._controlador_resultados.save(_resultados_obj)
        
    def eliminar_resultados (self,id):
        return self._controlador_resultados.delete(id)