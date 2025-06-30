# Definimos el diccionario
mi_diccionario = {
    'a': 53,
    'b': 44,
    'c': 91,
    'd': 17
}

# Extraer todos los valores
valores = list(mi_diccionario.values())

# Ordenar los valores de forma ascendente
valores_ordenados = sorted(valores)

# Imprimir los valores ordenados
print("Valores ordenados de manera ascendente:")
for valor in valores_ordenados:
    print(valor)
