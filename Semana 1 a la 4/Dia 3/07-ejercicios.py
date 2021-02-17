# Libro Algoritmos resueltos, pagina 138, ejercicios del 1 al 5

# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# for i in range(10):
#     print("HOLA", end="\n")

def dibujar_rectangulo():
    altura = int(input("Ingrese el alto: "))
    ancho = int(input("Ingrese el ancho: "))
    for numero in range(altura):
        for numero2 in range(ancho):
            print("*", end="")
        print("")
# dibujar_rectangulo(4,5)
# Escribir una funcion que nosotros le ingresemos el grosor de un hexagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
def dibujar_hexagono():
    lado = int(input("Ingrese el lado: "))
    tope = (2*(lado-1))+lado
    espacio = lado
    for numero in range(lado, tope+1, 2):
        espacio -= 1
        espacios = " "*espacio
        marca = "*"*numero
        if(numero == tope):
            limite = 0
            while(limite < lado):
                print(marca)
                limite += 1
            break
        print(espacios+marca)
    espacio += 1
    for numero in range(tope-2, lado-1, -2):
        espacios = " "*espacio
        espacio += 1
        marca = "*"*numero
        print(espacios+marca)

# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *
def triangulo_invertido():
    altura = int(input("Ingrese la altura: "))
    for fila in range(altura, 0, -1):
        print("*"*fila)
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12
def serie_collatz():
    numero = int(input("Ingrese el numero: "))
    
    while(numero != 1):
        if(numero % 2 == 0):
            numero /= 2
        else:
            numero *= 3+1
        print(numero)
# Una vez resuelto todos los ejercicios, crear un menu de seleccion que permita escoger que ejercicio queremos ejecutar hasta que escribamos "salir" ahi recien va a terminar de escoger el ejercicio
while(True):
    opc = input("Escoga la opcion del ejercicio o salir para salir del programa.\n\t1. Dibujar Rectangulo\n\t2. Dibujar Exagono\n\t3. Dibujar Triangulo Invertido\n\t4. Serie de Collatz\n\t5. Salir\n")
    if(opc == "1"):
        dibujar_rectangulo()
    elif(opc == "2"):
        dibujar_hexagono()
    elif (opc == "3"):
        triangulo_invertido()
    elif (opc == "4"):
        serie_collatz()
    else:
        print("Adios")
        break