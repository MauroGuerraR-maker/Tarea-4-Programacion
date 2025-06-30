#Definimos la funcion operar
def operar(a, b):
    try:
        return a + b       # Definimos uso normal
    except TypeError:
        print("Los tipos de datos no cuadran para hacer la operación.") #Definimos el mensaje de error en caso de no ser posible

def main():
    a = int(input("Ingrese un número: "))
    b = 'hola'
    operar(a, b)

main()
