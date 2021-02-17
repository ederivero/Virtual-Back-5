class Mueble:
    tipo="Futon"
    valor=00.00
    color="Transparente"
    especificaciones= ["Hecho en Perú", "Kaoba"]
    def devolver_especs(self):
        return self.especificaciones
# Crear un objeto o hacer una instancia de la clase Mueble
mueble1 = Mueble()
mueble2 = Mueble()
mueble1.tipo = "Dos cuerpos"
mueble2.devolver_especs()
print(mueble1.tipo)
print(mueble2.tipo)