import csv

# 1. Pedir al usuario el medio de pago
medio_pago = input("Ingrese el medio de pago (por ejemplo, Visa, Mastercard): ").strip()

# 2. Inicializar contador
contador = 0

# 3. Abrir el archivo CSV
with open("SalesJan2009.csv", "r", encoding="utf-8") as csvfile:
    lector = csv.DictReader(csvfile)
    for fila in lector:
        if fila["Payment_Type"].strip().lower() == medio_pago.lower():
            contador += 1

# 4. Mostrar resultado
print(f"Número de compras realizadas con {medio_pago}: {contador}")
