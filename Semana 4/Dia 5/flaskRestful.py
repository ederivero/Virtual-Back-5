from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
productos = []
# primero creo la instancia de mi clase API para poder declarar las rutas de mis Resource
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def start():
    return 'Bienvenido a mi API'

# el servicio restFul
class Producto(Resource):
    # crea un nuevo producto
    def post(self):
        # request.data devuelve todo lo que manda el front en formato texto plano
        # request.get_json() devuelve lo que me manda el front pero en formato de diccionario
        nuevoProducto = request.get_json()
        # metodo para agregar un nuevo item a una lista
        productos.append(nuevoProducto)
        return {
            'success': True,
            'content': productos,
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
                'message': 'Producto con id ${} no existe'.format(id)
            }, 400

    def put(self, id):
        return {}
    def delete(self, id):
        return {}

# Con el uso de flask_restful ya no se necesitan decoradores, solamente se declara el Resource y todas las rutas que querasmo que funciones para esos metodos
api.add_resource(Producto,'/producto','/otro')
api.add_resource(ProductoUnico, '/producto/<id>')
app.run(debug=True, port=5000)
