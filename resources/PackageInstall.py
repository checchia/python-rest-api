from flask_restful import Resource
import json


class PackageInstall(Resource):

    with open("package-config.json", 'r') as f:
        pkg_dict = json.load(f)

    def get(self, name):
        for k, v in self.pkg_dict.items():
            print(k, v)
            # print(self.pkg_dict["package"])
            #print(self.pkg_dict["service"])
            #print(self.pkg_dict["deploy"])
            #print(self.pkg_dict["hosts"])
        return {"message": "Package installation..." + name}
