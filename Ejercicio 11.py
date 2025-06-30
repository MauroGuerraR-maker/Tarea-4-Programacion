#Definimos la lista
lista = [1, 2, 3, 4]

try:
    # Intentar acceder a una posición que no existe
    elemento = lista[5]
    print("Elemento:", elemento)
except IndexError:
    print("Intenta acceder una posición que no está en el arreglo.") # Definimos un caso donde no sea posible cumplir con la peticion
