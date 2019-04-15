from flask_restful import Resource
import os

class PackageUpdate(Resource):

    def get(self, name):
        return {"message": "Package update for " + name}

    def post(self, name):
        from application import pkg_dict
        pkg = pkg_dict["package"]
        if name in pkg:
            print("Update command = ", pkg[name]["update"])
            os.system(pkg[name]["update"] + " " + name)
        return {"message": "Package update for " + name}
