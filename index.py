import imp
from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json
from controllers.mesasControler import AdministracionMesas
from controllers.partidosControler import AdministracionPartidos
from controllers.resultadosControler import AdministracionResultados
from controllers.candidatosControler import AdministracionCandidatos


mi_app = Flask (__name__)

_controler_usuario = AdministracionMesas()
_controler_partidos = AdministracionPartidos()
_controler_resultados = AdministracionResultados()
_controler_candidatos = AdministracionCandidatos()

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


#**********************Administracion Resultados ***************************************

#get

@mi_app.route('/resultados',methods=['GET'])
def mostrar_resultados():
    datos_salida = _controler_resultados.mostrar_resultados()
    
    return jsonify(datos_salida)
#post

@mi_app.route('/resultados',methods=['POST'])
def crear_resultados():
    datos_entrada = request.get_json()
    datos_salida = _controler_resultados.crear_resultados(datos_entrada)
    
    return jsonify(datos_salida)
#put

@mi_app.route('/resultados/<string:id>',methods=['PUT'])
def actualizar_resultados(id):  
    datos_entrada =request.get_json()
    json = _controler_resultados.actualizar_resultados (id,datos_entrada)
    
    return jsonify(json)


#delete

@mi_app.route('/resultados/<string:id>',methods=['DELETE'])
def eliminar_resultados(id):    
    datos_salida = _controler_resultados.eliminar_resultados(id)
    
    return jsonify(datos_salida)
#**********************administracion Candidatos ***************************************

#get

@mi_app.route('/candidatos',methods=['GET'])
def mostrar_candidato():
    datos_salida = _controler_candidatos.mostrar_candidato()
    
    return jsonify(datos_salida)
#post

@mi_app.route('/candidatos',methods=['POST'])
def crear_candidato():
    datos_entrada = request.get_json()
    datos_salida = _controler_candidatos.crear_candidato(datos_entrada)
    
    return jsonify(datos_salida)
#put

@mi_app.route('/candidatos/<string:id>',methods=['PUT'])
def actualizar_candidato(id):  
    datos_entrada =request.get_json()
    json = _controler_candidatos.actualizar_candidato (id,datos_entrada)
    
    return jsonify(json)


#delete

@mi_app.route('/candidatos/<string:id>',methods=['DELETE'])
def eliminar_candidato(id):    
    datos_salida = _controler_candidatos.eliminar_candidato(id)
    
    return jsonify(datos_salida)    
#**********************************************************

def cargar_configuracion():
    with open ("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor Ejecutandose...")
    serve (mi_app, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])
