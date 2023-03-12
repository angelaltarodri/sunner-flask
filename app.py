from flask import Flask

username = 'sunnerperu'
user_pass = '123456'

import growattServer
api = growattServer.GrowattApi(False, "my-user-id")
login_response = api.login(username, user_pass)
plant_list = api.plant_list(login_response['user']['id'])
plant_info_LEYTON = api.plant_info(1626659)

app = Flask(__name__)

@app.route("/")
def home():
    return plant_list

@app.route("/leyton")
def leyton():
    return plant_info_LEYTON

if __name__ == '__main__':
    app.run(debug=True, port=8001)