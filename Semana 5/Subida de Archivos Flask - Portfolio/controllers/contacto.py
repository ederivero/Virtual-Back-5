from flask_restful import Resource, reqparse
from models.contacto import ContactoModel

class ContactoController(Resource):
    serializer = reqparse.RequestParser(bundle_errors=True)
    serializer.add_argument(
        'contacto_nombre',
        type=str,
        required=True,
        help='Falta el contacto_nombre',
        location='json'
    )
    serializer.add_argument(
        'contacto_email',
        type=str,
        required=True,
        help='Falta el contacto_email',
        location='json'
    )
    serializer.add_argument(
        'contacto_fono',
        type=str,
        required=True,
        help='Falta el contacto_fono',
        location='json'
    )
    serializer.add_argument(
        'contacto_mensaje',
        type=str,
        required=True,
        help='Falta el contacto_mensaje',
        location='json'
    )
    serializer.add_argument(
        'contacto_fecha',
        type=str,
        required=True,
        help='Falta la contacto_fecha',
        location='json'
    )
    serializer.add_argument(
        'usuario_id',
        type=int,
        required=True,
        help='Falta el usuario_id',
        location='json'
    )
    def post(self):
        pass
    def get(self):
        pass