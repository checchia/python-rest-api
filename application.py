from flask import Blueprint
from flask_restful import Api
from resources.PackageInstall import PackageInstall
from resources.PackageUpdate import PackageUpdate
from resources.PackageRemove import PackageRemove
from resources.Service import Service
import json
import sys

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Load configuration file
pkg_dict = {}
with open("package-config.json", 'r') as f:
    pkg_dict = json.load(f)

# Route
api.add_resource(PackageInstall, '/install/<name>') # Route_1
api.add_resource(PackageRemove, '/remove/<name>') # Route_2
api.add_resource(PackageUpdate, '/update/<name>') # Route_2
api.add_resource(Service, '/restart/<name>') # Route_3

