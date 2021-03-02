# CREAR, EDITAR Y LEER (todas)
from flask_restful import Resource, reqparse
from models.redSocial import RedSocialModel

class RedSocialController(Resource):
    serializer = reqparse.RequestParser(bundle_errors=True)
    serializer.add_argument(
        'rs_nombre',
        type=str,
        required=True,
        help='Falta el rs_nombre',
        location='json'
    )
    serializer.add_argument(
        'rs_imagen',
        type=str,
        required=True,
        help='Falta el rs_imagen',
        location='json'
    )
    def post(self):
        pass
    def put(self):
        pass
    def get(self):
        pass