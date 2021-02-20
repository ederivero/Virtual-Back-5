# el parametro *args arguments es una lista dinamica de elementos para recibir un numero indeterminado de paramaetros
def hobbies(*atributos):
    print(atributos)
    for elemento in atributos:
        print(elemento)

# hobbies("bicicleta","puenting","rafting",20,["1",2,3])

# **kwargs "keywords arguments" es un parametro para recibir un numero ilimitado de parametros pero usando llave y valor (diccionario)
def personas(**kwargs):
    print(kwargs.get('nombre','no hay!'))
    # print(kwargs['nombre'])

    print(kwargs)

personas(nombre="eduardo", apellido="de rivero", mascotas=['lulu','morocha'], estatura=1.92)
personas(apellido="de rivero", mascotas=['lulu','morocha'], estatura=1.92)