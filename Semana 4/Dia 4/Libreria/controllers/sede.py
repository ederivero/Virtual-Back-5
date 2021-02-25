from flask_restful import Resource, reqparse
from models.sede import SedeModel
# basico
# get all sede
# create sede
# vincula una sede con varios libros y viceversa (un libro con varias sedes)
serializer = reqparse.RequestParser(bundle_errors=True)
serializer.add_argument(
    'sede_latitud',
    type=float,
    required=True,
    help='Falta la sede_latitud',
    location='json',
    dest='latitud'
)
serializer.add_argument(
    'sede_ubicacion',
    type=str,
    required=True,
    help='Fata la sede_ubicacion',
    location='json',
    dest='ubicacion'
)
serializer.add_argument(
    'sede_longitud',
    type=float,
    required=True,
    help='Falta la sede_longitud',
    location='json',
    dest='longitud' # es como se va a llamar una vez que hemos usado el metodo parse_args()
)
class SedesController(Resource):
    def post(self):
        data = serializer.parse_args()
        print(data)
        # LOS TIPOS DE DATOS QUE NO SON NI NUMERICOS NI STRINGS = DECIMAL, FECHA, NO PUEDE HACER LA CONVERSION AUTOMATICA
        nuevaSede = SedeModel(data['ubicacion'],data['latitud'], data['longitud'])
        nuevaSede.save()
        return {
            'success': True,
            'content': nuevaSede.json(),
            'message': 'Se creo la sede exitosamente'
        }, 201
    def get(self):
        pass




# busqueda de todos los libros de una sede 
# busqueda de todos los libros de una sede segun su categoria