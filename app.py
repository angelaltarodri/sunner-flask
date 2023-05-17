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
user_pass = 'abc123'

CORS(app)

api = growattServer.GrowattApi(False, "my-user-id")

@app.route("/")
def home():
    login_response = api.login(username, user_pass, False)
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

@app.route("/dashboard/<int:plantId>/<string:metric>")
def plant_dashboard(plantId, metric):
    try:
        datetoday = datetime.date.today()
        print(plantId)
        print(metric)
        if metric == 'h':
            timespan = Timespan.hour
            dashboard_data = api.dashboard_data(plantId, timespan, datetoday)
            return dashboard_data
        elif metric == 'd':
            timespan = Timespan.day
            dashboard_data = api.dashboard_data(plantId, timespan, datetoday)
            return dashboard_data
        elif metric == 'm':
            timespan = Timespan.month
            dashboard_data = api.dashboard_data(plantId, timespan, datetoday)
            return dashboard_data
        elif metric == 'y':
            dateyearago = datetoday - datetime.timedelta(days=365)

            timespan = Timespan.month
            dd1 = api.dashboard_data(plantId, timespan, datetoday)
            y1 = datetoday.year
            dd2 = api.dashboard_data(plantId, timespan, dateyearago)
            y2 = dateyearago.year
            dashboard_data = {
                "detailsDataCurrentYear": {
                    "year": y1,
                    "data":dd1, 
                },
                "detailsDataYearAgo": {
                    "year":y2,
                    "data": dd2
                }
            }
            return jsonify(dashboard_data)
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route("/details/<int:plantId>/<string:metric>")
def plant_details(plantId, metric):
    try:
        datetoday = datetime.date.today()
        print(plantId)
        print(metric)
        timespan = Timespan.day

        if metric == 'm':
            timespan = Timespan.month
        # hora, dia y mes
        details_data = api.plant_detail(plantId, timespan, datetoday)
        return details_data
    except ValueError as e:
        return jsonify(message=str(e)), 400

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)