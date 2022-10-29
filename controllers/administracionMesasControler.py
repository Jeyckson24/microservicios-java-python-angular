from model.administracionMesaModelo import AdministracionMesa

class AdministracionMesas():
    def __init__(self):
        pass
    
    def mostrar_mesas (self):
        datos_mesa={
            "id":"1",
            "Puesto de votacion":"Colegio Rufino Centro",
            "Mesa #":"1"
        }
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