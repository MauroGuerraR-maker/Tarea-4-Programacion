import json

# 1. Leer el archivo JSON con las notas
with open("notas.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# 2. Pedir al usuario el código del estudiante
codigo = input("Ingrese el código del estudiante: ").strip()

# 3. Verificar si el código existe
if codigo not in datos:
    print("El código ingresado no existe en el archivo.")
else:
    # 4. Obtener las notas
    notas = datos[codigo]

    # 5. Calcular el promedio
    promedio = sum(notas) / len(notas)

    # 6. Crear el nuevo diccionario con el promedio
    resultado = {codigo: promedio}

    # 7. Guardar el resultado en un nuevo archivo JSON
    with open("promedio_estudiante.json", "w", encoding="utf-8") as fout:
        json.dump(resultado, fout, ensure_ascii=False, indent=2)

    print(f"Promedio calculado y guardado en 'promedio_estudiante.json': {promedio:.2f}")
