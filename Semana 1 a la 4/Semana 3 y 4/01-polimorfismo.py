# El poliformismo es tener el mismo metodo (nombre) pero que, dependiendo de su clase en la que se encuentra va a tener un comportamiento diferente
class Vehiculo:
    # pass
    def __init__(self, peso):
        self.peso = peso
    def movilidad(self):
        print("Me muevo en muchas ruedas")
class Automovil(Vehiculo):
    def movilidad(self):
        print("Me muevo en 4 ruedas")
    # def movilidad(self, parametro):
    #     print("OTRO COMPORTAMIENTO")
class Bicicleta(Vehiculo):
    def movilidad(self):
        print("Me muevo en 2 ruedas")
class Patines(Vehiculo):
    def movilidad(self):
        print("Me muevo en 6 ruedas")
miAuto = Automovil(14)
miAuto.movilidad()
miBici = Bicicleta(15)
miBici.movilidad()
