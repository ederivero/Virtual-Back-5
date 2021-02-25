from flask_restful import Resource, reqparse
from models.libro import LibroModel

serializer = reqparse.RequestParser()
serializer.add_argument(
    'libro_nombre',
    type=str,
    required=True,
    help='Falta el libro_nombre',
    location='json'
)
serializer.add_argument(
    'libro_cant',
    type=int,
    required=True,
    help='Falta el libro_cant',
    location='json'
)
serializer.add_argument(
    'libro_edicion',
    type=str,
    required=True,
    help='Falta el libro_edicion',
    location='json'
)
serializer.add_argument(
    'autor_id',
    type=int,
    required=True,
    help='Falta el autor_id',
    location='json'
)
serializer.add_argument(
    'categoria_id',
    type=int,
    required=True,
    help='Falta el categoria_id',
    location='json'
)


class LibrosController(Resource):
    def post(self):
        data = serializer.parse_args()
        nuevoLibro = LibroModel(data['libro_nombre'],data['libro_cant'], data['libro_edicion'], data['autor_id'], data['categoria_id'])
        nuevoLibro.save()
        return {
            'success': True,
            'content': nuevoLibro.json(),
            'message':'Se creo el libro exitosamente'
        }, 201
    def get(self):
        libros = LibroModel.query.all()
        print(libros[0].autorLibro.json())
        resultado = []
        for libro in libros:
            resultadoTemporal = libro.json()
            resultadoTemporal['autor'] = libro.autorLibro.json()
            resultadoTemporal['categoria'] = libro.categoriaLibro.json()
            del resultadoTemporal['autor_id'] # forma para eliminar una llave de un diccionario
            del resultadoTemporal['categoria_id']
            resultado.append(resultadoTemporal)
            # resultado.append(libro.autorLibro.json())
        return {
            'success': True,
            'content': resultado,
            'message': None
        }

