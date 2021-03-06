from flask_restful import Resource, reqparse
from models.contacto import ContactoModel
from config.utils import enviarCorreo
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
        data = self.serializer.parse_args()
        nuevoContacto = ContactoModel(data['contacto_nombre'],data['contacto_email'], data['contacto_fono'], data['contacto_mensaje'], data['usuario_id'])
        nuevoContacto.save()
        if enviarCorreo(data['contacto_email'],data['contacto_nombre']):
            return {
                'success':True,
                'content': None,
                'message': 'Se agrego la solicitud exitosamente'
            }
        else:
            return{
                'success': False,
                'content': None,
                'message': 'Hubo un error al enviar el correo pero se guardo exitosamente la solicitud'
            }
    def get(self):
        pass