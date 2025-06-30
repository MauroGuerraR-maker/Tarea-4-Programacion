import json

# Cargar el JSON desde el archivo, en donde: 
# open(...): Abre el archivo personas.json en modo lectura ("r").
# encoding="utf-8": Para que pueda leer caracteres especiales (tildes, ñ).
# json.load(f): Convierte el contenido del archivo JSON en un diccionario de Python y lo guarda en la variable datos.

with open("Credenciales.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# 1. Buscar personas que practican un deporte dado:
# input(...): Lee el deporte que escribe el usuario.
# strip(): Quita espacios al principio y al final.
# capitalize(): Pone la primera letra en mayúscula (para estandarizar).

deporte_input = input("Ingrese el deporte a buscar: ").strip().capitalize()

print("\nPersonas que practican", deporte_input + ":")

for usuario, info in datos.items():
    if deporte_input in [d.capitalize() for d in info["deportes"]]:
        print(f"- {info['nombres']} {info['apellidos']}")

# 2. Buscar personas en un rango de edad
edad_min = int(input("\nIngrese la edad mínima: "))
edad_max = int(input("Ingrese la edad máxima: "))

print(f"\nPersonas con edad entre {edad_min} y {edad_max}:")

for usuario, info in datos.items():
    if edad_min <= info["edad"] <= edad_max:
        print(f"- {info['nombres']} {info['apellidos']}")

# 3. Crear JSON de deportes con usuarios
deportes_dict = {}

for usuario, info in datos.items():
    for deporte in info["deportes"]:
        deporte_cap = deporte.capitalize()
        if deporte_cap not in deportes_dict:
            deportes_dict[deporte_cap] = []
        deportes_dict[deporte_cap].append(usuario)

# Guardar el JSON resultante
# Abre el archivo deportes_personas.json en modo escritura ("w").
# json.dump(...) escribe el diccionario en formato JSON:
# ensure_ascii=False: Permite tildes y caracteres especiales.
#indent=2: Formatea con indentación de 2 espacios.

with open("deportes_personas.json", "w", encoding="utf-8") as f:
    json.dump(deportes_dict, f, ensure_ascii=False, indent=2)

print("\nSe creó el archivo 'deportes_personas.json' con la lista de deportes.")
