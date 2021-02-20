from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# https://flask-cors.readthedocs.io/en/latest/
from flask_cors import CORS

app = Flask(__name__)
productos = []
# primero creo la instancia de mi clase API para poder declarar las rutas de mis Resource
api = Api(app)
# si yo quiero permitir todos los accesos a todos los metodos y de cualquier dominio y cualquier header
# para indicar que recursos (resource) pueden ser accedidos se tiene que indicar que endpoint y que origenes pueden ser accedidos
# https://docs.python.org/3/library/re.html
CORS(app,
    # resource captura un diccionario en la llave se debe indicar los endpoints que vamos a declarar seguido de su lista de argumentos en el cual pueden ser los "origins" (origenes), "methods" (metodos), "headers" (cabeceras), defecto: * 
    #  resources={r"/producto/*":{"origins":"*"}, "/almacen":{"origins":"mipagina.com"}}, 
    #  origins=['mipagina.com','otrapagina.com'], # sirve para indicar que dominios pueden acceder a mi API, defecto: *
    #  methods=['POST', 'PUT', 'DELETE', 'GET'], # para indicar que metodos pueden acceder a nuesta API , por defecto el GET siempre va a poder, defecto: *
     )
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