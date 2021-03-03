from flask import Flask, request
from config.base_datos import bd
from models.usuario import UsuarioModel
from models.categoria import CategoriaModel
from models.redSocial import RedSocialModel
from models.usuarioRedSocial import UsuarioRedSocialModel
from models.contacto import ContactoModel
from models.conocimiento import ConocimientoModel
# srive para que el nombre del archivo que me manda el cliente lo valide antes de guardar y evita que se guarde nombre con caracteres especiales que puedan malograr el funcionamiento de mi api
from werkzeug.utils import secure_filename 
import os
from uuid import uuid4 # es un codigo unico irrepetible
app = Flask(__name__)
# ALTER USER 'userame'@'url' IDENTIFIED WITH mysql_native_password BY 'password';
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
# mysql://username:password@host:port/base_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/portfolioFlask'
# sirve para evitar el warning de seguimiento de las modificaciones a la bd que en un futuro generará costos de memoria significativos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bd.init_app(app)
bd.create_all(app=app)

# sirve para indicar en que parte del proyecto se va a almacenar los archivos subidos
UPLOAD_FOLDER= 'media'
EXTENSIONES_PERMITIDAS_IMAGENES = ['jpg', 'png', 'jpeg']

def filtro_extensiones(filename):
    # el metodo rsplit puede recibir dos parametros, el primer parametro es el caracter a divir y el segundo opcional es el que especifica en cuantas partes debe de ser dividido
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
    if filtro_extensiones(archivo.filename):
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


if __name__ == '__main__':
    app.run(debug=True)