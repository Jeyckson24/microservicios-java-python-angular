from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Api gateway'

@app.route("/login")
def inicio_sesion():
    return "path login api gateway"


if __name__ == '__main__':
    app.run()
