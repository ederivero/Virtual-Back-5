# setter = ingresar el valor a un atributo
# getter = devolver el valor del atributo
# deletter = elimina el atributo de una clase
class Persona:
    def __init__(self):
        self.__nombre=''
    def __setnombre(self, nombre):
        print('el setnombre() ha sido llamado')
        self.__nombre = nombre
    def __getnombre(self):
        print('el getnombre() ha sido llamado')
        return self.__nombre
    def __deletenombre(self):
        print('el deletenombre() ha sido llamado')
        del self.__nombre
    # funcion property para definir nuestras funciones de get, set y delete
    name = property(__getnombre, __setnombre, __deletenombre)

objPersona = Persona()
objPersona.name = 'Eduardo'
print(objPersona.name)
del objPersona.name

