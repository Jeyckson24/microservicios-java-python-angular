from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Api gateway'

@app.route("/login")
def inicio_sesion():
    return "path login api gateway"


def cargar_configuracion():
    with open ("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor Ejecutandose... en "+datos_configuracion["url-api-gateway"]+str (datos_configuracion["puerto-api-gateway"]))
    serve (app, host=datos_configuracion["url-api-gateway"], port=datos_configuracion["puerto-api-gateway"])
