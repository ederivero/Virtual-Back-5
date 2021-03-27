class Mesa:
    # color = "rojo"
    # capacidad = 4
    def __init__(self, valor1="rojo", valor2=4):
        self.color = valor1
        self.capacidad = valor2


objMesa1 = Mesa("azul", 10)
objMesa1.color = "verde"

objMesa2 = Mesa()
print(objMesa2.color)
print(objMesa1.color)
