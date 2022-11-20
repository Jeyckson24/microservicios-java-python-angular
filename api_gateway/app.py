import datetime

from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
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
