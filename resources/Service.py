from flask_restful import Resource


class Service(Resource):
    def get(self, name):
        return {"message": "Service control..." + name}
