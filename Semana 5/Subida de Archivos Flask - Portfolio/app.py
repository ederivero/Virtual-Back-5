from flask import Flask
from config.base_datos import bd
from models.usuario import UsuarioModel
from models.categoria import CategoriaModel
from models.redSocial import RedSocialModel
from models.usuarioRedSocial import UsuarioRedSocial
from models.contacto import ContactoModel
from models.conocimiento import ConocimientoModel
app = Flask(__name__)
# mysql://username:password@host:port/base_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/portfolioFlask'
# sirve para evitar el warning de seguimiento de las modificaciones a la bd que en un futuro generará costos de memoria significativos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bd.init_app(app)
bd.create_all(app=app)

@app.route('/uploadFile')
def subir_archivo():
    pass


if __name__ == '__main__':
    app.run(debug=True)