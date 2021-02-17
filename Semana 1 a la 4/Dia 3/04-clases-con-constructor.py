class Persona:
    def __init__(self, nombre, fecnac):
        self.nombre = nombre
        self.fecha_nacimiento = fecnac

    def saludar(self):
        print(f"hola {self.nombre}")
    
    def fechaNacimiento(self):
        print(f"tu fecha de nacimiento es {self.fecha_nacimiento}")

persona1 = Persona("Eduardo","01 de agosto de 1992")
persona1.saludar()
persona1.fechaNacimiento()



# crear una clase persona que tenga de atributos sus datos personales (nombre,apellido,edad) y su experiencia laboral , que se ingrese por un menu la opc 1 para ingresar nueva experiencia laboral, que la opc 2 la muestre y que la opc 3 la elimine todas las experiencias y que la opcion 4 salga del programa
class PersonaEjercicio:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.experiencias=[]
    def ingresar_experiencia(self, experiencia):
        self.experiencias.append(experiencia)
    def mostrar_experiencia(self):
        print("las experiencias son",self.experiencias)
    def eliminar_experiencias(self):
        self.experiencias.clear()

objPersona = PersonaEjercicio("eduardo","de rivero","32")
opcion = 0
while opcion!=4:
    try:
        opcion = int(input("""Ingrese una opcion
        1. Ingresar experiencia
        2. Mostrar experiencia
        3. Eliminar todas las experiencias
        4. Salir
        """))
        if opcion == 1:
            experiencia = input("Ingrese la experiencia: ")
            objPersona.ingresar_experiencia(experiencia=experiencia)
        elif opcion == 2:
            objPersona.mostrar_experiencia()
        elif opcion == 3:
            objPersona.eliminar_experiencias()
        elif opcion == 4:
            print("Adios")
        else:
            print("INGRESA SOLO OPCIONES DEL 1 AL 5")
    except:
        print("Ingresa solo numeros!")


