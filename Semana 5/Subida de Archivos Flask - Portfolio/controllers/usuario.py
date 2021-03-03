from flask_restful import Resource, reqparse

class RegistroController(Resource):
    serializer = reqparse.RequestParser(bundle_errors=True)
    serializer.add_argument(
        'usuario_nombre',
        type=str,
        required=True,
        help='Falta el usuario_nombre',
        location='json'
    )
    serializer.add_argument(
        'usuario_apellido',
        type=str,
        required=True,
        help='Falta el usuario_apellido',
        location='json'
    )
    serializer.add_argument(
        'usuario_correo',
        type=str,
        required=True,
        help='Falta el usuario_correo',
        location='json'
    )
    serializer.add_argument(
        'usuario_titulo',
        type=str,
        required=True,
        help='Falta el usuario_titulo',
        location='json'
    )
    serializer.add_argument(
        'usuario_info',
        type=str,
        required=True,
        help='Falta el usuario_info',
        location='json'
    )
    serializer.add_argument(
        'usuario_cv',
        type=str,
        required=True,
        help='Falta el usuario_cv',
        location='json'
    )
    serializer.add_argument(
        'usuario_superuser',
        type=str,
        required=True,
        help='Falta el usuario_superuser',
        location='json'
    )
    serializer.add_argument(
        'usuario_password',
        type=str,
        required=True,
        help='Falta el usuario_password',
        location='json'
    )