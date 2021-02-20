from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
app = Flask(__name__)
productos = []
# primero creo la instancia de mi clase API para poder declarar las rutas de mis Resource
api = Api(app)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def start():
    return 'Bienvenido a mi API'



serializer = reqparse.RequestParser()
serializer.add_argument(
    'producto_nombre',
    type=str,
    required=True,
    help='Falta el producto_nombre',
    location='json'
)
serializer.add_argument(
    'producto_precio',
    type=float,
    required=True,
    help='Falta el producto_precio',
    location='json'
)
serializer.add_argument(
    'producto_cantidad',
    type=int,
    required=True,
    help='Falta el producto_cantidad',
    location='json'
)
# el servicio restFul
class Producto(Resource):
    # crea un nuevo producto
    def post(self):
        # request.data devuelve todo lo que manda el front en formato texto plano
        # request.get_json() devuelve lo que me manda el front pero en formato de diccionario
        # nuevoProducto = request.get_json()
        nuevoProducto = serializer.parse_args()

        # metodo para agregar un nuevo item a una lista
        productos.append(nuevoProducto)
        return {
            'success': True,
            'content': nuevoProducto,
            'message': 'Producto creado exitosamente'
        }, 201
    # devolver todos los productos
    def get(self):
        return {
            'success': True,
            'content': productos,
            'message': None
        }

class ProductoUnico(Resource):
    # https://developer.mozilla.org/es/docs/Web/HTTP/Status
    def get(self, id):
        # devolver producto segun su id
        logitud = len(productos)
        if logitud > id:
            return {
                'success': True,
                'content': productos[id],
                'message': None
            }
        else:
            return {
                'success': False,
                'content': None,
                'message': 'Producto con id {} no existe'.format(id)
            }, 400

    def put(self, id):
        # mediante el metodo parse_args() recien se hace la validacion de los parametros solicitados y si todo esta bien, devolvera los argumentos en forma de un diccionario
        # primero validar si existe el producto con ese id(posicion)
        longitud = len(productos)
        data = serializer.parse_args()
        if longitud > id:
            #existe
            productos[id] = data
            return {
                'success': True,
                'content': productos[id],
                'message': 'Producto actualizado con exito'
            }, 201
        else:
            #no existe
            return {
                'success': False,
                'content': None,
                'message': 'Producto con id {} no existe'.format(id)
            }, 400
    def delete(self, id):
        longitud = len(productos)
        if longitud > id:
            #existe
            productos.pop(id)
            return {
                'success': True,
                'content': None,
                'message': 'Producto eliminado con exito'
            }, 201
        else:
            #no existe
            return {
                'success': False,
                'content': None,
                'message': 'Producto con id {} no existe'.format(id)
            }, 400

# Con el uso de flask_restful ya no se necesitan decoradores, solamente se declara el Resource y todas las rutas que querasmo que funciones para esos metodos
api.add_resource(Producto,'/producto','/otro')
api.add_resource(ProductoUnico, '/producto/<int:id>')
app.run(debug=True, port=5000)
# lo que hacemos aca abajo nunca se va a ejecutar