# Para definir variables numericas
numero = 1
numerodecimal = 18.5

# Variables de tipo texto
texto = 'Soy un texto'
otrotexto= "Soy otro texto"

# Para saber que tipo de variable es
print(type(numerodecimal))
# Para mostrar algo en la consola print()
print(1,2,3)

# Para definir una variable tiene que comenzar con una letra NUNCA con un numero
# Hay dos clases de variables, variables MUTABLES, variables INMUTABLES
# MUTABLES => son las variables que se van a modificar y todas sus referencias van a sufrir los cambios (List, dict, tuples)
# INMUTABLES => son las que se van a modificar solamente una determinada variable sin que las otras que copiaron su valor también lo hagan (int, str, float, bool, etc)

# Para eliminar una variable
del texto
variable1 = 10
variable2 = 10.5
variable3 = True
variable4 = "Texto"

# Para definir varias variables en una sola linea de codigo
# nombre = Eduardo apellido = de Rivero
nombre, apellido = "Eduardo", "de Rivero"
edad, nacionalidad = (35, "Peruano")
print(nombre)
print(apellido)

# La variable con valor None es una variable sin tipo y esta esperando cambiar de valor para tener un tipo definido
variablex = None

# Variables inmutables
a=10
b=a
a=20
print(b,a)

# Variables mutables
c = [10,15]
d = c
c[0]=15
print(d)