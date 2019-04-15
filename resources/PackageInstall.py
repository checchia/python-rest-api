from flask_restful import Resource
import os


class PackageInstall(Resource):

    def get(self, name):
        return {"message": "Package installation."}
    
    def post(self, name):
        from application import pkg_dict
        pkg = pkg_dict["package"]
        if name in pkg:
            print("Installation command = ", pkg[name]["install"])
            os.system(pkg[name]["install"] + " " + name)
        return {"message": "Package installation for " + name}
