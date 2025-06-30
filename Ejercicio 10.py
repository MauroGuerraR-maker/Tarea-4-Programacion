import json

# 1. Diccionario de reemplazo
reemplazos = {
    "$": "a",
    "#": "e",
    "*": "i",
    "¬": "o",
    "+": "u"
}

# 2. Leer el archivo JSON con las cadenas encriptadas
with open("CadenasEncriptadas.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# 3. Crear un diccionario para las cadenas desencriptadas
desencriptadas = {}

# 4. Procesar cada cadena
for clave, texto in datos.items():
    cadena_descifrada = texto
    # Reemplazar cada símbolo por su vocal correspondiente
    for simbolo, vocal in reemplazos.items():
        cadena_descifrada = cadena_descifrada.replace(simbolo, vocal)
    desencriptadas[clave] = cadena_descifrada

# 5. Guardar el resultado en un nuevo archivo JSON
with open("cadenas_desencriptadas.json", "w", encoding="utf-8") as fout:
    json.dump(desencriptadas, fout, ensure_ascii=False, indent=2)

print("Archivo 'cadenas_desencriptadas.json' creado con las cadenas desencriptadas.")
