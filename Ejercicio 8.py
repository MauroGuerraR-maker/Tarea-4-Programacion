import json

# 1. Leer el primer archivo JSON
with open("archivo1.json", "r", encoding="utf-8") as f1:
    datos1 = json.load(f1)

# 2. Leer el segundo archivo JSON
with open("archivo2.json", "r", encoding="utf-8") as f2:
    datos2 = json.load(f2)

# 3. Crear un diccionario para las coincidencias
coincidencias = {}

# 4. Recorrer las claves del primer diccionario
for clave, valor in datos1.items():
    # Si la clave existe en el segundo y el valor es idéntico
    if clave in datos2 and datos2[clave] == valor:
        coincidencias[clave] = valor

# 5. Guardar el resultado en un nuevo JSON
with open("coincidencias.json", "w", encoding="utf-8") as fout:
    json.dump(coincidencias, fout, ensure_ascii=False, indent=2)

print("Archivo 'coincidencias.json' creado con las coincidencias exactas.")
