from flask import Flask
from flask import jsonify

from flask_cors import CORS
import sys
import logging

import growattServer

app = Flask(__name__)

username = 'sunnerperu'
user_pass = '123456'

CORS(app)

api = growattServer.GrowattApi(False, "my-user-id")

@app.route("/")
def home():
    login_response = api.login(username, user_pass)
    plant_list = api.plant_list(login_response['user']['id'])
    return plant_list

# 1654546
# 1626659
# 1581547

@app.route("/<int:plantId>")
def plant_info(plantId):
    try:
        plant_info = api.plant_info(plantId)
        return plant_info
    except ValueError as e:
        return jsonify(message=str(e)), 400

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)