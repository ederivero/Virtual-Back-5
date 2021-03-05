# funcion para customizar el mensaje de error al usar JWT
def manejo_error_jwt(error):
    print(error.status_code) # sirve para devolver el status code del error actual
    print(error.error) # me retorna el error que se ha sucitado 
    print(error.description) # la descripcion del error
    print(error.headers) # la cabecera de ese error
    return {
        'success': False
    }, 400