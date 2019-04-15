from flask_restful import Resource
import os

class Service(Resource):
    
    def get(self, name):
        return {"message": "Service control."}
    
    def post(self, name):
        from application import pkg_dict
        pkg = pkg_dict["package"]
        if name in pkg:
            print("Service control command = ", pkg[name]["command"])
            os.system(pkg[name]["remove"] + " " + name)
        return {"message": "Service control " + name}
