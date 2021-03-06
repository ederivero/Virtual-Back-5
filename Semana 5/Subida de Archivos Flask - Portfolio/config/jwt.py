# funcion para customizar el mensaje de error al usar JWT
def manejo_error_jwt(error):
    print(error.status_code) # sirve para devolver el status code del error actual
    print(error.error) # me retorna el error que se ha sucitado 
    print(error.description) # la descripcion del error
    print(error.headers) # la cabecera de ese error (solamente aparece cuando no hay token)
    respuesta = {
        'success': False,
        'content': None,
        'message': None
    }
    if error.error == 'Invalid token':
        respuesta['message'] = 'Token invalida'
    elif error.error == 'Authorization Required':
        respuesta['message'] = 'Se necesita una token para esta peticion'
    else:
        respuesta['message'] = 'Sucedio otro error, comuniquese con el backend'
    
    return respuesta, 401