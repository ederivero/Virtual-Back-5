from flask import Flask, request, send_file
from flask_restful import Api
from config.base_datos import bd
from controllers.usuario import RegistroController, LoginController
from controllers.categoria import CategoriaController
from controllers.redSocial import RedSocialController
from models.usuarioRedSocial import UsuarioRedSocialModel
from models.contacto import ContactoModel
from models.conocimiento import ConocimientoModel
# srive para que el nombre del archivo que me manda el cliente lo valide antes de guardar y evita que se guarde nombre con caracteres especiales que puedan malograr el funcionamiento de mi api
from werkzeug.utils import secure_filename 
import os
from uuid import uuid4 # es un codigo unico irrepetible
from flask_jwt import JWT, jwt_required, current_identity
from config.seguridad import autenticador, identificador
from config.jwt import manejo_error_jwt
from datetime import timedelta

app = Flask(__name__)
api = Api(app)

# ALTER USER 'userame'@'url' IDENTIFIED WITH mysql_native_password BY 'password';
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
# mysql://username:password@host:port/base_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/portfolioFlask'
# sirve para evitar el warning de seguimiento de las modificaciones a la bd que en un futuro generará costos de memoria significativos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='miclavesecreta' # esto usa FLASK-JWT para encriptar la token, esta sera la contraseña para encriptar y desencriptar la token
app.config['JWT_AUTH_URL_RULE']='/iniciarSesion' # para modificar la ruta de autenticacion
app.config['JWT_AUTH_USERNAME_KEY']='correo' # para modificar la llave del username
app.config['JWT_AUTH_PASSWORD_KEY']='contraseña' # para modificar la llave del password
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer' # para modificar la cabecera (la palabra antes de la token) en la que se pasa la token
app.config['JWT_EXPIRATION_DELTA']= timedelta(minutes=10) # para modificar el tiempo de vida de la token

jsonwebtoken = JWT(app=app, authentication_handler=autenticador, identity_handler=identificador)
jsonwebtoken.jwt_error_callback = manejo_error_jwt # para modificar el manejo de errores que puede dar la token

bd.init_app(app)
# bd.drop_all(app=app)

bd.create_all(app=app)

# sirve para indicar en que parte del proyecto se va a almacenar los archivos subidos
UPLOAD_FOLDER= 'media'
EXTENSIONES_PERMITIDAS_IMAGENES = ['jpg', 'png', 'jpeg']

def filtro_extensiones(filename):
    # el metodo rsplit puede recibir dos parametros, el primer parametro es el caracter a divir y el segundo opcional es el que especifica en cuantas partes debe de ser dividido
    # nos va a indicar si es true o false si es que la extension de nuestro archivo hace MATCH con alguno de la lista de extensiones permitidas
    return '.' in filename and \
            filename.rsplit('.', 1)[-1].lower() in EXTENSIONES_PERMITIDAS_IMAGENES


@app.route('/uploadFile', methods=['POST'])
def subir_archivo():
    print(request.files)
    # primero validamos que nos este pasando en el form-data la llave archivo
    if 'archivo' not in request.files:
        return {
            'success': False,
            'message': 'No hay archivo para subir',
            'content': None
        }, 400
    archivo = request.files['archivo']
    # luego validamos que la llave archivo contengan un archivo
    if archivo.filename == '':
        return {
            'success': False,
            'message': 'No hay archivo para subir',
            'content': None
        }, 400
    print(filtro_extensiones(archivo.filename))
    if filtro_extensiones(archivo.filename) is False:
        return {
            'success': False,
            'message': 'Archivo no permitido',
            'content': None
        }, 400
    # asi extraigo el formato del archivo antes de modificar su nombre
    formato = archivo.filename.rsplit(".")[-1]
    print(archivo.filename.rsplit("."))
    # como hago para obtener la ultima posicion de una lista en python
    nombre_modificado = str(uuid4())+'.'+formato
    nombre_archivo = secure_filename(nombre_modificado)
    # este es el proceso para guardar el archivo en el servidor
    archivo.save(os.path.join(UPLOAD_FOLDER,nombre_archivo))
    return {
        'success': True,
        'message': 'Se guardo el archivo exitosamente',
        'content': nombre_archivo
    }, 201

@app.route('/devolverImagen/<string:nombre>', methods=['GET'])
def devolver_archivo(nombre):
    # el metodo send_file sirve para mandar cualquier tipo de archivos, si es un archivo imagen se mostrara caso contrario se descargará
    try:
        return send_file(os.path.join(UPLOAD_FOLDER, nombre))
    except:
        return send_file(os.path.join(UPLOAD_FOLDER, 'default.png'))

@app.route('/eliminarImagen/<string:nombre>', methods=['DELETE'])
def remove_file(nombre):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER,nombre))
        return {
            'success':True,
            'content': 'Imagen eliminada exitosamente'
        }
    except:
        return {
            'success': False,
            'content': 'No se encontro la imagen a eliminar'
        }

@app.route('/protegida')
@jwt_required()
def mostrar_saludo():
    print(current_identity)
    return {
        'mensaje': 'Hola!'
    }


api.add_resource(RedSocialController, '/redsocial')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(CategoriaController, '/categoria')

if __name__ == '__main__':
    app.run(debug=True)