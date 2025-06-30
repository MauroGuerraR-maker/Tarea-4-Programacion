# Lista de personas a utilizar
personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Ana María", "apellidos": "Pérez Gómez", "edad": 45},
    {"nombres": "Juan Carlos", "apellidos": "Rodríguez Díaz", "edad": 30},
    {"nombres": "Sergio Javier", "apellidos": "Martínez López", "edad": 18},
    {"nombres": "Camila Andrea", "apellidos": "Rengifo Rodriguez", "edad": 22},
    {"nombres": "Alejandro", "apellidos": "Martin Alonso", "edad": 71},
    {"nombres": "Maria Estefania", "apellidos": "Alvarado Gomez", "edad": 10}
]

# Obtener rango de edades al usuario
edad_min = int(input("Ingrese la edad mínima: "))
edad_max = int(input("Ingrese la edad máxima: "))

print("\nPersonas en el rango de edad:")

# Recorrer la lista y filtrar personas
for persona in personas:
    if edad_min <= persona["edad"] <= edad_max:
        print(f"- {persona['nombres']} {persona['apellidos']}")
