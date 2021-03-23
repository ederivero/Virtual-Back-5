# pip3 install flask
# pip3 list
from flask import Flask

# __name__ sirve para definir que nuestra aplicacion de Flask se va a ejecutar en el hilo principal del compilador de python
app = Flask(__name__)

# siempre para indicar el comportamiento de una ruta tiene que ir en un decorador y luego definir su funcion con todo su comportamiento adentro
@app.route('/')
def inicio():
    print("hola")
    return 'El servidor se ha levantado exitosamente'

# para que cuando nosotros hagamos algun cambio en nuestra aplicacion, al momento de guardarse se reinicie el servidor
# la condicional __name__ == __main__ sirve muy parecido al void main(){}, es decir sirve para usar la parte principal del compilador
if __name__ == '__main__':
    app.run(debug=True)

