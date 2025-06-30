import csv
import zipfile

# 1. Descomprimir el archivo ZIP
zip_path = "SalesJan2009.csv.zip"
csv_filename = "SalesJan2009.csv"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall()  # Extrae en el directorio actual

# 2. Pedir al usuario el país a buscar
pais = input("Ingrese el país: ").strip()

# 3. Contar las compras realizadas en ese país
contador = 0

with open(csv_filename, "r", encoding="utf-8") as csvfile:
    lector = csv.DictReader(csvfile)
    for fila in lector:
        if fila["Country"].strip() == pais:
            contador += 1

# 4. Mostrar el resultado
print(f"Número de compras realizadas en {pais}: {contador}")
