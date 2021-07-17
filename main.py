from flask import Flask
from flask_restful import Api

from controllers.ip_check_api import IpCheck

app = Flask(__name__)
api = Api(app)

api.add_resource(IpCheck, "/v2/ip-check")

if __name__ == "__main__":
    app.run()
