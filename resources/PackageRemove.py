from flask_restful import Resource


class PackageRemove(Resource):


    def get(self, name):
        return {"message": "Package removal..." + name}
