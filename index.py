import imp
from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json
from controllers.mesasControler import AdministracionMesas
from controllers.partidosControler import AdministracionPartidos

mi_app = Flask (__name__)

_controler_usuario = AdministracionMesas()
_controler_partidos = AdministracionPartidos()
#**********************administracion Mesas ***************************************

#get

@mi_app.route('/mesas',methods=['GET'])
def mostrar_mesas():
    datos_salida = _controler_usuario.mostrar_mesas()
    
    return jsonify(datos_salida)
#post

@mi_app.route('/mesas',methods=['POST'])
def crear_mesa():
    datos_entrada = request.get_json()
    datos_salida = _controler_usuario.crear_mesa(datos_entrada)
    
    return jsonify(datos_salida)
#put

@mi_app.route('/mesas/<string:id>',methods=['PUT'])
def actualizar_mesa(id):  
    datos_entrada =request.get_json()
    json = _controler_usuario.actualizar_mesa (id,datos_entrada)
    
    return jsonify(json)


#delete

@mi_app.route('/mesas/<string:id>',methods=['DELETE'])
def eliminar_mesa(id):    
    datos_salida = _controler_usuario.eliminar_mesa(id)
    
    return jsonify(datos_salida)


#**********************administracion Partidos ***************************************

#get

@mi_app.route('/partidos',methods=['GET'])
def mostrar_partidos():
    datos_salida = _controler_partidos.mostrar_partidos()
    
    return jsonify(datos_salida)
#post

@mi_app.route('/partidos',methods=['POST'])
def crear_partido():
    datos_entrada = request.get_json()
    datos_salida = _controler_partidos.crear_partido(datos_entrada)
    
    return jsonify(datos_salida)
#put

@mi_app.route('/partidos/<string:id>',methods=['PUT'])
def actualizar_partido(id):  
    datos_entrada =request.get_json()
    json = _controler_partidos.actualizar_partido (id,datos_entrada)
    
    return jsonify(json)


#delete

@mi_app.route('/partidos/<string:id>',methods=['DELETE'])
def eliminar_partido(id):    
    datos_salida = _controler_partidos.eliminar_partido(id)
    
    return jsonify(datos_salida)


def cargar_configuracion():
    with open ("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor Ejecutandose...")
    serve (mi_app, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])