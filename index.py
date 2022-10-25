import imp
from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json
from controllers.administracionUsuariosControler import AdministracionUsuarios
mi_app = Flask (__name__)

_controler_usuario = AdministracionUsuarios()
#get

@mi_app.route('/usuarios',methods=['GET'])
def mostrar_usuario():
    datos_salida = _controler_usuario.mostrar_usuario()
    
    return jsonify(datos_salida)
#post

@mi_app.route('/usuarios',methods=['POST'])
def crear_usuario():
    datos_entrada = request.get_json()
    datos_salida = _controler_usuario.crear_usuario(datos_entrada)
    
    return jsonify(datos_salida)
#put

@mi_app.route('/usuarios/<string:id>',methods=['PUT'])
def actualizar_usuario(id):  
    datos_entrada =request.get_json()
    json = _controler_usuario.actualizar_usuario (id,datos_entrada)
    
    return jsonify(json)


#delete

@mi_app.route('/usuarios/<string:id>',methods=['DELETE'])
def eliminar_usuario(id):    
    datos_salida = _controler_usuario.eliminar_usuario(id)
    
    return jsonify(datos_salida)

def cargar_configuracion():
    with open ("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor Ejecutandose...")
    serve (mi_app, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])
    
    