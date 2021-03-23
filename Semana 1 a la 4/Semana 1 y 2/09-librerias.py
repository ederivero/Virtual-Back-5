# pip3 install nombre_paquete
# pip3 list (lista todas las librerias instaladas en nuestra maquina)
# pip3 freeze (nos indica las librerias pero de una manera mas tecnica, usada para el deploy)

# Importa toda la libreria y puedo usar toda su funcionalidad
import camelcase

# Selecciono que clase, funcion, etc voy a utilizar de esa libreria
# from camelcase import CamelCase

# Igual que la forma anterior pero le puedo dar un alias a esa clase, funcion, etc para que sea mas facil de usar
# from camelcase import CamelCase as Camello

camello = camelcase.CamelCase()
texto = "hola amigos feliz miercoles"
print(camello.hump(texto))