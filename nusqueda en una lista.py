# Lista de números
numeros = [1, 3, 5, 7, 9, 11, 13]

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número: "))

# Verificar si el número pertenece a la lista
if numero_ingresado in numeros:
    print(f"{numero_ingresado} pertenece a la lista.")
else:
    print(f"{numero_ingresado} no pertenece a la lista.")
