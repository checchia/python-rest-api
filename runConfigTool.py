from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class PackageInstall(Resource):
    def get(self):
        return {"message": "Package installation"}

class PackageRemove(Resource):
    def get(self):
        return {"message": "Package removal ..."}

class Restart(Resource):
    def get(self, name):
        return {"message": "Restarting a given service ..."}

api.add_resource(PackageInstall, '/install') # Route_1
api.add_resource(PackageRemove, '/remove') # Route_2
api.add_resource(Restart, '/restart/<name>') # Route_3


if __name__ == '__main__':
     app.run()
