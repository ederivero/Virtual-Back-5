codigo = "virtual4"
# El metodo print va a recoger un numero ilimitado de parametros separados por "," y siempre entre coma y coma va a imprimir un espacio en blanco
print(codigo,"otra cosa")
# MODO II
alumnos = 38
print("Estoy en el curso {} y hay {} alumnos".format(codigo, alumnos))
# MODO III Modificando el orden a imprimir
print("Tengo {1} alumnos del curso {0}".format(codigo, alumnos))
# MODO IV 
print(f"Tengo {alumnos} alumnos en el curso {codigo}")
# MODO V RESTRINGIR LA CANTIDAD DE DECIMALES DE UNA VARIABLES
pi = 3.14151564654654654654
print(f"El valor de pi es: {pi:1.3f}")