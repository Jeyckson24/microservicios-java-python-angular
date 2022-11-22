import datetime
import re

from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
import requests
import json



app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "**secret**"  # Change this!
jwt = JWTManager(app)

@app.route("/login",methods=["POST"])
def inicio_sesion():
    datos_entrada = request.get_json()
    configuracion = cargar_configuracion()
    headers = {"Content-Type":'application/json; charset=utf8'}
    respuesta = requests.post(configuracion["url-ms-seguridad"]+"/user/login",json=datos_entrada)
    print(configuracion["url-ms-seguridad"]+"/user/login")
    print(respuesta.status_code)
    print(respuesta.json())

    if respuesta.status_code == 200:
        usuario = respuesta.json()
        tiempo_caducidad_token = datetime.timedelta(60*60*24)
        token_acceso = create_access_token(identity=usuario, expires_delta=tiempo_caducidad_token)
        return {"token_acceso": token_acceso}
    else:
        return jsonify({"mensaje": "Error usuario o contraseña"})

@app.before_request
def verificar_peticion():
    print("ejecucion de callback")
    print("url->",request.url)
    print("metodo->", request.method)

    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]

    if excludedRoutes.__contains__(request.path):

        pass

    elif verify_jwt_in_request():
        usuario = get_jwt_identity()


        if usuario ["rol"] is not None:
            tienePermiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            print(usuario["rol"]["_id"])

            if not  tienePermiso:
                return jsonify({"menssage":"Rol no tiene permiso"}),401

        else:
            return jsonify({"message":"No tiene Rol asignado - Permiso Denegado"}),401

def limpiarURL(url):
    partes =url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url =url.replace(laParte,"?")
    return url

def validarPermiso(endPoint, metodo, idRol):
    configuracion = cargar_configuracion()
    url =configuracion["url-ms-seguridad"] + "/rolpermiso/" +str(idRol)
    print(url)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }

    response = requests.post( url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True

    except:

        pass
    return tienePermiso

#############  PATHS DE CONSULTA ####################

@app.route('/permisos/listar', methods=["GET"])
def permisos_listar ():
    print("Consulta candidatos")
    return jsonify({"respuesta":"path permisos"})

@app.route('/candidatos', methods=["GET"])
def candidatos_listar ():
    headers = {"Content_Type":"application/json; charset=utf8"}
    configuracion = cargar_configuracion()

    url =configuracion["url-ms-resultados"] + "/candidatos"
    respuesta = requests.get(url,headers=headers)
    print("Consulta candidatos")
    return jsonify(respuesta.json())


############# FIN PATHS DE CONSULTA ##################
@app.route('/')
def home ():
    return 'api gateway'
def cargar_configuracion():
    with open ("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor Ejecutandose... en "+datos_configuracion["url-api-gateway"]+str (datos_configuracion["puerto-api-gateway"]))
    serve (app, host=datos_configuracion["url-api-gateway"], port=datos_configuracion["puerto-api-gateway"])
