from flask import Flask
from config.base_datos import bd
from models.autor import AutorModel
from models.categoria import CategoriaModel
from models.libro import LibroModel
from models.sede import SedeModel
app = Flask(__name__)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
#                                    formato://username:password@host:port/databasename
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/flasklibreria'
# si tu servidor no tiene contraseña, ponlo asi:
# 'mysql://root:@localhost:3306/flasklibreria'
# para evitar el warning de la funcionalidad de sqlalchemy de track modification:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicio la aplicacion proveyendo las credenciales indicadas en el app.config pero aun no se ha conectado a la bd
bd.init_app(app)
# recien se conecta a la bd, pero necesita el driver para poder conectarse
# para conectarnos a una base de datos en mysql deberemos instalar el driver: pip install mysqlclient
bd.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=True)
