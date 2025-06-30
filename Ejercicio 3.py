def mezclar_diccionarios(dic1, dic2):
    """
    Mezcla dos diccionarios.
    Si hay claves repetidas, se conserva el valor de dic1.
    """
    # Empezar con una copia de dic2
    resultado = dic2.copy()
    # Actualizar con los elementos de dic1 (sobrescriben los de dic2 si hay coincidencia)
    resultado.update(dic1)
    return resultado

# Ejemplo de uso
d1 = {'a': 1, 'b': 2, 'c': 4, 'e': 9}
d2 = {'b': 99, 'c': 3, 'd': 8, 'f': 10}

mezcla = mezclar_diccionarios(d1, d2)

print("Diccionario resultante:", mezcla)
