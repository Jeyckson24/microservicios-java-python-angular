from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json

app = Flask(__name__)


@app.route("/login",methods=["POST"])
def inicio_sesion():
    datos_entrada = request.get_json()
    configuracion = cargar_configuracion()
    respuesta = request.post(configuracion["url-ms-seguridad"]+"/user/login",json=datos_entrada)
    print(configuracion["url-ms-seguridad"]+"/usuarios/login")
    print(respuesta.status_code)
    print(respuesta.json())
    return "path login api gateway"

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
