# Definimos la funcion main
def main():
    dicc = {'James': 'Java', 'Dennis': 'C', 'Das': 'Python'}
    try:
        print(dicc['Ada']) 
    except KeyError:        # Establecemos un mensaje de error al no encontrar una llave que no existe en el diccionario
        print("Intenta acceder una llave que no está en el diccionario.")

main()
