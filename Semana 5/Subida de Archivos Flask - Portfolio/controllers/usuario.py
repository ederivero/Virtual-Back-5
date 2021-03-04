from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel
import bcrypt
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
        type=bool,
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
    serializer.add_argument(
        'usuario_foto',
        type=str,
        required=True,
        help='Falta el usuario_foto',
        location='json'
    )
    def post(self):
        data = self.serializer.parse_args()
        nuevoUsuario = UsuarioModel(data['usuario_nombre'], 
                    data['usuario_apellido'], 
                    data['usuario_correo'],
                    data['usuario_password'],
                    data['usuario_titulo'], 
                    data['usuario_info'], 
                    data['usuario_cv'], 
                    data['usuario_superuser'],
                    data['usuario_foto'])
        nuevoUsuario.save()
        return {
            'success':True,
            'content': nuevoUsuario.json(),
            'message': 'Usuario creado exitosamente'
        }, 201


class LoginController(Resource):
    # implementar el login
    serializer = reqparse.RequestParser(bundle_errors=True)
    serializer.add_argument(
        'correo',
        type=str,
        required=True,
        help='Falta el correo',
        location='json'
    )
    serializer.add_argument(
        'password',
        type=str,
        required= True,
        help='Falta el password',
        location='json'
    )
    def post(self):
        data = self.serializer.parse_args()
        print(data)
        # filtrar el usuario por su correo y ver si existe o no existe
        usuario = UsuarioModel.query.filter_by(usuarioCorreo=data['correo']).first()
        print(usuario)
        if(usuario):
            # ver si la contraseña es correcta
            password = bytes(data['password'],'utf-8')
            hash = bytes(usuario.usuarioPassword,'utf-8')
            if bcrypt.checkpw(password, hash): # esto me retorna un True si la contraseña es correcta y un False si es que es diferente
                print('las contraseñas son iguales')
            else:
                print('las contraseñas no coinciden')
        return {
            'success': True
        }