from flask import Flask
from flask_cors import CORS

import growattServer

username = 'sunnerperu'
user_pass = '123456'

api = growattServer.GrowattApi(False, "my-user-id")
login_response = api.login(username, user_pass)
plant_list = api.plant_list(login_response['user']['id'])

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return plant_list

@app.route("/<string:plantId>")
def leyton(plantId):
    plant_info = api.plant_info(plantId)
    return plant_info

@app.route("/cortez")
def gabo():
    plant_info = api.plant_info(1581547)
    return plant_info

if __name__ == '__main__':
    # app.run(debug=True, port=8001)
    app.debug = True
    app.run()