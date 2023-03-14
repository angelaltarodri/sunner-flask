from flask import Flask
from flask import jsonify

from flask_cors import CORS
import sys
import logging

import growattServer

app = Flask(__name__)

username = 'sunnerperu'
user_pass = '123456'

api = growattServer.GrowattApi(False, "my-user-id")
login_response = api.login(username, user_pass)
plant_list = api.plant_list(login_response['user']['id'])
CORS(app)


@app.route("/")
def home():
    return jsonify(plant_list)


@app.route("/<string:plantId>")
def leyton(plantId):
    if not plantId.isnumeric():
        return jsonify(message="Plant ID inválido")
    plant_info = api.plant_info(plantId)
    return jsonify(plant_info)


@app.route("/gabo")
def gabo():
    plant_info = api.plant_info(1581547)
    return jsonify(plant_info)


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.secret_key = "Mi clave super mega secreta"
