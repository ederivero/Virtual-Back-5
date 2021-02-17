# excepsiones => try ... except ... *** else ... finally ...
# https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=Python%20%2D%20Error%20Types,usually%20along%20with%20the%20reason.
try:
    # todo el codigo que sea escrito adentro tendra un manejo de por si sucede algo malo, y si sucede algo malo el except va a evitar que el programa se cuelgue
    numero1 = input("ingrese un primer numero: ")
    numeroEntero = int(numero1)
    numero2 = int(input("Ingrese un segundo numero: "))
    print(numeroEntero/numero2)
except ZeroDivisionError:
    print('No puedes ingresar 0 como divisor')
except ValueError:
    print('Ingresa un numero y no letras')
except :
    print(EnvironmentError)
    print('Algo debiste haber hecho mal, intenta nuevamente')
else:
    # ingresa al else cuando no ingreso a ninguna except
    print("todo funciono correctamente")
finally:
    # no le importa si todo salio bien o si hubo un error
    print("yo me ejecuto si o si")
print('Yo soy otra parte del codigo')

# x = 0
# arreglo = []
# while x<10:
#     try:
#         num=int(input("ingrese un numero: "))
#         arreglo.append(num)
#         x = x + 1
#     except:
#         print('ingresa un numero!!')

# print(arreglo)


