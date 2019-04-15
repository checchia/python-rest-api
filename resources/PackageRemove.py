from flask_restful import Resource
import os

class PackageRemove(Resource):

    def get(self, name):
        return {"message": "Package removal of " + name}

    def post(self, name):
        from application import pkg_dict
        pkg = pkg_dict["package"]
        if name in pkg:
            print("Removal command = ", pkg[name]["remove"])
            os.system(pkg[name]["remove"] + " " + name)
        return {"message": "Package removal of " + name}
