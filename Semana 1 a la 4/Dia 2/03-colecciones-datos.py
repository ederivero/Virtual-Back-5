# LISTAS
# en js se le dice ARRAY
colores = ["rojo","blanco", "azul", "violeta"]
print(colores)
# Imprime la ultima posicion de la lista
print(colores[-1])
# Imprimir desde la 0 hasta la <2
print(colores[0:2])
# Imprimir desde la 1 hasta el final
print(colores[1:])

# La forma de copiar el contenido (y ya no estan alojados en la misma posicion de memoria)
# EN js se utiliza los variables2 = ...variable
colores2 = colores[:]
# colores[0]="verde"
# print(colores2)
# print(colores)

# Todas las formas de impresion de las LISTAS sirven para los textos
nombre = "Eduardo"
# print(nombre[2])

# Metodo para agregar un nuevo valor dentro de la lista
colores.append("negro")
# Metodo para quitar un valor de la lista
colores.remove("blanco")
# para el metodo pop(indice) saca el elemento de la lista segun su posicion y nos da la opcion de almacenarlo en una variable
color_eliminado = colores.pop(2)
print(color_eliminado)
print(colores)
del colores[1]
print(colores)
# Metodo para resetear toda la lista y dejarla en blanco
colores.clear()
print(colores)

# TUPLAS => coleccion de elementos ordenada QUE NO SE PUEDE MODIFICAR
# es inalterable y sirve para usar elementos que nunca se van a modificar
nombres = ("Eduardo", "RICK", "LIZBETH")
# nombres[1]= "Martin"
# Logitud de la tupla
print(len(nombres))

# Ver si hay elementos repetidos en una tupla
print(nombres.count("EDUARDO"))

# CONJUNTOS => coleccion de elementos desordenada, osea que no tiene indice para acceder a sus elementos
estaciones = {"VERANO", "OTOÑO", "INVIERNO", "PRIMAVERA"}
print(estaciones)
# la forma de iterar es mediante un FOR
estaciones.add("OTOÑOVERANO")
print(estaciones)

# DICCIONARIOS => coleccion de elementos que estan indexados, no estan ordenados por una posicion en concreto sino que manejan una llave y un valor
persona = {
    'id':1,
    "nombre":"Roberto",
    "fecnac": "01/01/2001",
    "relacion":"soltero",
    "hobbies":{
        "nombre":"Futbol",
        "dificultad":"Basico"
    }
}
variable = """
Esto es un texto
que respesta los saltos de linea
y se usa mayormente para documentación
"""
print(persona["id"])
persona.pop("id")
del persona['nombre']
persona["apellido"]="Medina"
print(persona["hobbies"]["dificultad"])
print(variable)