# funcion que no recibe parametros
def saludar():
    """FUNCION QUE TE SALUDA"""
    print("Hola buenas noches")

saludar()
# las funciones pueden recibir cuantos parametros nosotros deseemos
def saludarConNombre(nombre):
    print(f"hola {nombre}")

saludarConNombre("eduardo")

# si queremos que un parametro sea opcional de dar su valor, le podemos definir el valor PREDETERMINADO al momento de definir la funcion
# Todos los parametros que son opcionales de recibir valor SIEMPRE van despues de los que no son opcionales
def saludoOpcional(apellido, nombre=None):
    if nombre:
        print(f"Hola {nombre} {apellido}")
    else:
        print(f"Hola {apellido}")
    # Hola incognito

saludoOpcional("Martinez")
saludoOpcional("rodriguez","Eduardo")

def suma(num1, num2):
    """Función que recibe dos numeros y retorna su sumatoria"""
    return num1+num2
    # todo lo que pongamos despues del return nunca se va a ejecutar
    print("Hola")

resultado = suma(5,2)
print(resultado)

# el parametro *args arguments es una lista dinamica de elementos para recibir un numero indeterminado de paramaetros
def hobbies(*args):
    print(args)
    for elemento in args:
        print(elemento)

hobbies("bicicleta","puenting","rafting",20,["1",2,3])

# **kwargs "keywords arguments" es un parametro para recibir un numero ilimitado de parametros pero usando llave y valor (diccionario)
def personas(**kwargs):
    print(kwargs)

personas(nombre="Eduardo",apellido="De Rivero", mascotas=False, estatura=1.89)

def indeterminada(*args, **kwargs):
    print(args)
    print(kwargs)

indeterminada(5,"juan","otoño",False, pais="Peru",epoca="republicana")

def sacar_igv(igv):
    pass


# FUNCIONES LAMBDA
# PEQUEÑA y ANONIMA
#NOMBRE   = lambda PARAM:  RETURN(rpta)
resultado = lambda numero: numero+30
resultado2 = lambda numero1, numero2: numero1+numero2
print(resultado(10))
print(resultado2(80,20))
# GENERALMENTE SE USA PARA OPERACIONES CORTAS DE UN MAXIMO DE UNA LINEA DE RESOLUCION
