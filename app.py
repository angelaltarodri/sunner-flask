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
    return plant_list

# 1654546
# 1626659
# 1581547

@app.route("/<string:plantId>")
def plant_info(plantId):
    if not plantId.isnumeric():
        return jsonify(message="Plant ID inválido")
    try:
        plant_info = api.plant_info(plantId)
        return plant_info
    except ValueError:
        return jsonify(message="Error al decodificar el objeto JSON"), 400

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)