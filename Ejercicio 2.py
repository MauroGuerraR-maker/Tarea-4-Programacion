def verificar_inclusion(diccionario1, diccionario2):
    """
    Verifica si todas las claves y valores de diccionario1 están en diccionario2.
    """
    for clave, valor in diccionario1.items():
        # Si la clave no existe o el valor no coincide, retorna False
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False
    return True

# Ejemplo de uso
diccionario_1 = {
    'x': 10,
    'y': 20,
    'z': 30  
}

diccionario_2 = {
    'x': 10,
    'y': 20,
    'z': 30
}

resultado = verificar_inclusion(diccionario_1, diccionario_2)

if resultado:
    print("Todas las claves y valores de diccionario_1 están en diccionario_2.")
else:
    print("No todas las claves y valores de diccionario_1 están en diccionario_2.")
