from models.usuario import UsuarioModel
import bcrypt

class Usuario(object):
    def __init__(self, id, username):
        self.id= id
        self.username= username
    
    def __str__(self):
        return "Usuario con el id='%s' y username='%s'" % (self.id, self.username)

def autenticador(username, password):
    """Este es el metodo encargado en mi JWT de validar que las credenciales fueron ingresadas correctamente"""
    if username and password:
        # ahora valido si ese usuario existe en la base de datos
        usuario = UsuarioModel.query.filter_by(usuarioCorreo=username).first()
        if usuario:
            if bcrypt.checkpw(bytes(password,'utf-8'), bytes(usuario.usuarioPassword,'utf-8')):
                print('correctamente logeado')
                return Usuario(usuario.usuarioId, usuario.usuarioCorreo)
            else:
                print('La contraseña no coincide')
                return None
        else:
            print('No se encontro usuario')
            return None
    else:
        print('Falta el usuario o la password')
        return None

def identificador(payload):
    """El identificador sirve para que, una vez el usuario ya logeado, pueda hacer peticiones a una ruta protegida y este será el encargado de identificar a dicho usuario y devolver su informacion al controlador a consultar"""
    # el payload es un diccionario en el cual la identidad del usuario (id) se guarda en su llave "identity"
    print(payload)
    if(payload['identity']):
        usuario = UsuarioModel.query.filter_by(usuarioId=payload['identity']).first()
        if usuario:
            return (usuario.usuarioId, usuario.usuarioCorreo, usuario.usuarioSuperUser)
        else:
            # el usuario en la token no existe en mi bd (eso es imposible!)
            return None
    else:
        # en mi payload no hay nada almacenado en mi llave identity 
        return None