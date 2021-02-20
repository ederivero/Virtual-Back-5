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
    def post(self):
        # request.data devuelve todo lo que manda el front en formato texto plano
        # request.get_json() devuelve lo que me manda el front pero en formato de diccionario
        print(request.get_json()) 
        print('ingreso al post')
        return {
            'success': True,
            'content': [],
            'message': 'Producto creado exitosamente'
        }

# Con el uso de flask_restful ya no se necesitan decoradores, solamente se declara el Resource y todas las rutas que querasmo que funciones para esos metodos
api.add_resource(Producto,'/producto','/otro')
app.run(debug=True, port=5000)
