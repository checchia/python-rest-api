from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.PackageInstall import PackageInstall
from resources.PackageRemove import PackageRemove
from resources.Service import Service

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(PackageInstall, '/install/<name>') # Route_1
api.add_resource(PackageRemove, '/remove/<name>') # Route_2
api.add_resource(Service, '/restart/<name>') # Route_3

