from flask import Flask
from flask_restful import Api
from config.base_datos import bd
# from models.autor import AutorModel
from controllers.autor import AutoresController
from models.categoria import CategoriaModel
from models.libro import LibroModel
from models.sede import SedeModel
from models.sedeLibro import SedeLibroModel
app = Flask(__name__)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
#                                    formato://username:password@host:port/databasename
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/flasklibreria'
api = Api(app)

# si tu servidor no tiene contraseña, ponlo asi:
# 'mysql://root:@localhost:3306/flasklibreria'
# para evitar el warning de la funcionalidad de sqlalchemy de track modification:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicio la aplicacion proveyendo las credenciales indicadas en el app.config pero aun no se ha conectado a la bd
bd.init_app(app)
# con drop all se eliminan todas las tablas MAPEADAS en el proyecto
bd.drop_all(app=app)
# recien se conecta a la bd, pero necesita el driver para poder conectarse
# para conectarnos a una base de datos en mysql deberemos instalar el driver: pip install mysqlclient
bd.create_all(app=app)

# RUTAS DE MI API RESTFUL
api.add_resource(AutoresController, '/autores')

if __name__ == '__main__':
    app.run(debug=True)
