# CREAR, EDITAR Y LEER (todas)
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse, request
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
    @jwt_required()
    def post(self):
        print(current_identity)
        # solamente un usuario que es super usuario puede hacer un registro, sino indicar que no tiene los privilegios suficientes
        identidad_usuario = current_identity
        if(identidad_usuario['usuario_superuser']):
            data = self.serializer.parse_args()
            nuevaRedSocial = RedSocialModel(data['rs_nombre'], data['rs_imagen'])
            nuevaRedSocial.save()
            return {
                'success': True,
                'content': nuevaRedSocial.json(),
                'message': 'Se creo la nueva red social'
            }
        else:
            return {
                'success': False,
                'content': None,
                'message': 'Usuario no dispone de suficientes privilegios'
            }, 500
    def put(self):
        pass
    def get(self):
        # host => me retorna el dominio
        # host_url => me retorna el dominio en formato url
        # print(request.host)
        # print(request.host_url)
        redesSociales = RedSocialModel.query.all()
        resultado = []
        for redSocial in redesSociales:
            temporal = redSocial.json()
            temporal['rs_imagen'] = request.host_url+'devolverImagen/'+temporal['rs_imagen']
            resultado.append(temporal)
        return {
            'success': True,
            'content': resultado,
            'message': None
        }