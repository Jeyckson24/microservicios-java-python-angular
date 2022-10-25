from model.administracionUsuariosModelo import AdministracionUsuarios

class AdministracionUsuarios():
    def __init__(self):
        pass
    
    def mostrar_usuario (self):
        datos_usuario={
            "id":"1",
            "nombre":"jjeyckson",
            "apellido":"chacon"
        }
        return datos_usuario
    
    
    def crear_usuario (self,datos_entrada):
        _usuario = AdministracionUsuarios(datos_entrada)
        return _usuario.__dict__
        
        
        
    def actualizar_usuario (self,datos_entrada):
        usuario = AdministracionUsuarios(datos_entrada)
        return usuario.__dict__
        
    def eliminar_usuario (self,id):
        respuesta = {
            "respuesta": "Usuario con codigo" + id + "eliminado"
        }
        return respuesta