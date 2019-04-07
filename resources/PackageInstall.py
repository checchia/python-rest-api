from flask_restful import Resource
import json


class PackageInstall(Resource):

    with open("package-config.json", 'r') as f:
        pkg_dict = json.load(f)

    def get(self, name):
        for distro in self.pkg_dict:
            print(distro['Name'])
        return {"message": "Package installation..." + name}
