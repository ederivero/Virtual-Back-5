from flask import Flask, request
app = Flask(__name__)
supermercados = []
@app.route('/')
def inicio():
    return 'El servidor funciona exitosamente'
# GET => SE USA PARA SOLICITAR INFORMACION
# POST => SE USA PARA CREAR NUEVA INFORMACION
# PUT => SE USA PARA ACTUALIZAR ALGUN REGISTRO
# DELETE => SE USA PARA ELIMINAR ALGUN REGISTRO
# por defecto el unico metodo (verbo) permitido si no le indicamos va ser el GET
@app.route('/supermercado',methods=['GET','POST'])
def ingresar_supermercado():
    print(request.method)
    if request.method == 'GET':
        return {
            'ok': True,
            'content': supermercados,
            'message': None
        }
    elif request.method == 'POST':
        # metodo get_json() convierte lo que me llega por el body a un diccionario en python
        print(request.get_json())
        informacion = request.get_json()
        supermercados.append(informacion)
        return {
            'ok':True,
            'content':supermercados,
            'message': 'Se agrego exitosamente el supermercado'
        }, 201


# type(variable) == int
@app.route('/supermercado/<int:id_super>', methods=['GET','PUT','DELETE'])
def supermercadoPorId(id_super):
    # print(type(id_super))
    # if request.method == 'GET':
    #     # como verifico que el id que me mande exista en mi lista
    #     print(len(supermercados))
    #     if len(supermercados) > id_super:
    #         return {
    #             'ok':True,
    #             'content':supermercados[id_super],
    #             'message': None
    #         }
    #     else:
    #         return {
    #             'ok':False,
    #             'content':None,
    #             'message': 'El supermercado con posicion {} no existe'.format(id_super)
    #         }

    if len(supermercados) > id_super:
        # el supermercado con el id id_super si existe
        if request.method == 'GET':
            return {
            'ok':True,
            'content':supermercados[id_super],
            'message': None
            }
        # IMPLEMENTAR LA LOGICA DEL PUT Y DELETE
        elif request.method == 'PUT':
            data = request.get_json()
            supermercados[id_super] = data
            return {
                'ok':True,
                'content':supermercados[id_super],
                'message': 'Se actualizo el supermercado exitosamente'
            }, 201
        elif request.method == 'DELETE':
            supermercados.pop(id_super)
            # del supermercados[id_super]
            return {
                'ok': True,
                'content': None,
                'message': 'Se elimino exitosamente el supermercado'
            }, 204
    else:
        return {
            'ok':False,
            'content':None,
            'message': 'El supermercado con posicion {} no existe'.format(id_super)
        }


if __name__== '__main__':
    app.run(debug=True)