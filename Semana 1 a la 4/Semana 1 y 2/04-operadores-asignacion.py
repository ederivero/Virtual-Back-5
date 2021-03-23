# OPERADORES DE ASIGNACION
# = Igual
# += Incremento => variable = variable + 1 | variable += 1
# -= Decremento => variable -= 1
# *= Multiplicacion => variable *= 4
# /= Division => variable /= 10
# ** Potencia => variable**5
variable1= 10
variable2= 20
variable1 += variable2
print(variable1)

# Operadores de Comparación
# == es igual que
# != es diferente que
# <, > es menor que, es mayor que
# <=, >= es menor o igual que, es mayor o igual que
num1, num2 = 15, 25
print(num1> num2)

# Operadores Logicos
# and = si todo es verdadero, es verdadero, de lo contrario es falso
# or = basta con que un valor sea verdadero para que todo sea verdadero
# not = es lo inverso al resultado
# EN JAVASCRIPT AND = &&, or = ||
print((10>=10) and (10>20))
print((10>=10) or (10>20))
print(not(10>=10) or (10>20))