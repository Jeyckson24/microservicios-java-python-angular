from model.candidatos import Candidatos
from repositorios.repositorioCandidatos import RepositorioCandidatos


class AdministracionCandidatos():
    def __init__(self):
        self._controlador_candidato = RepositorioCandidatos()
    
    def mostrar_candidato (self):
        datos_candidato= self._controlador_candidato.findAll()
        return datos_candidato
    
    
    def crear_candidato (self,datos_entrada):
        _candidato = Candidatos(datos_entrada)
        return self._controlador_candidato.save(_candidato)
        
    def actualizar_candidato (self,id,datos_entrada):
        _candidato_db =self._controlador_candidato.findById(id)
        _candidato_obj = Candidatos(_candidato_db)
        _candidato_obj.codigo = datos_entrada["codigo"]
        _candidato_obj.candidato = datos_entrada["candidato"]
        _candidato_obj.partido = datos_entrada["partido"]
        return self._controlador_candidato.save(_candidato_obj)
        
    def eliminar_candidato (self,id):
        return self._controlador_candidato.delete(id)