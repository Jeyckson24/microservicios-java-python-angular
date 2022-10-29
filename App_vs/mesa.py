class mesa(ABC):
    def __init__(self,codigo,mesa,puestovotacion):
        self.codigo         = codigo
        self.mesa           = mesa
        self.puestovotacion = puestovotacion
        
    def imprimir_mesa(self):
        return self.codigo + " " + self.mesa + " " + self.puestovotacion
  
        
    def __str__(self):
        return self.codigo + " " + self.mesa + " " + self.puestovotacion