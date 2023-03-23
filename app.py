import datetime
from flask import Flask
from flask import jsonify

from flask_cors import CORS
import sys
import logging

import growattServer
from growattServer import Timespan

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

@app.route("/details")
def plant_detail():
    try:
        # # dia y mes
        # plant_detail = api.plant_detail(1626659, Timespan.day, datetime.datetime(2023, 3, 20, 12, 0) )
        # hora, dia y mes
        dashboard_data = api.dashboard_data(1626659, Timespan.day, datetime.datetime(2023, 3, 20))
        return dashboard_data
    except ValueError as e:
        return jsonify(message=str(e)), 400

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)