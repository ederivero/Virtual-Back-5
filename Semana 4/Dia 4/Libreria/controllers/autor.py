from flask_restful import Resource, reqparse
from models.autor import AutorModel
serializer = reqparse.RequestParser()
serializer.add_argument(
    'autor_nombre',
    type=str,
    required= True,
    help='Falta el autor_nombre'
)

class AutoresController(Resource):
    def post(self):
        informacion = serializer.parse_args()
        "INSERT INTO T_AUTOR (AUTOR_NOMBRE) VALUES (INFORMACION['AUTOR_NOMBRE'])"
        # creamos una nueva instancia de nuestro modelo del Autor pero aun no se ha creado en la bd, esto sirve para validar que los campos ingresados cumplan con las definiciones de las columnas
        nuevoAutor = AutorModel(informacion['autor_nombre'])
        # ahora si se guarda en la bd, si hubiese algun problema dara el error de la BD pero ese indice (pk) si es autoincrementable salta una posicion
        nuevoAutor.save()
        print(nuevoAutor)
        return {
            'success': True,
            'content': None,
            'message': 'Autor creado exitosamente'
        }, 201
        