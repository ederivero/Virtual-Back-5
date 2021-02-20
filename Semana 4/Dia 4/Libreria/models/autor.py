from config.base_datos import bd
# https://docs.sqlalchemy.org/en/13/core/type_basics.html?highlight=datatypes
# Si aun no sabemos que tipos de datos podemos utilizar en sqlalchemy podemos usar:
# from sqlalchemy import types
class AutorModel(bd.Model):
    # para cambiar el nombre de la tabla a crearse
    __tablename__= "t_autor"
    autorId = bd.Column(
                        name="autor_id", # Nombre de la col en la bd
                        type_=bd.Integer, # tipo de dato en la bd
                        primary_key=True, # setear si va a ser pk o no
                        autoincrement= True, # setear si va a ser AI o no 
                        nullable= False, # setear si va a admitir valores nulos o no
                        unique=True, # si no se va a repetir el valor o no
                        )
    autorNombre = bd.Column(name="autor_nombre", type_=bd.String(45))

    def __init__(self, nombreAutor):
        self.autorNombre = nombreAutor
    
    def save(self):
        # el metodo session devuelve la sesion actual y evita que se cree una nueva sesion y asi relentizar la conexion a mi bd
        # el metodo add sirve para agregar toda mi instancia (mi nuevo autor) a un formato que sea valido para la bd
        bd.session.add(self)
        # el commit sirve para que los cambios realizados a la bd se hagan efecto, esto generalmente se usa con transacciones
        bd.session.commit()