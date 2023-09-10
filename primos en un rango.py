def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_en_rango(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Solicitar al usuario que ingrese el rango
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

# Generar y mostrar los números primos en el rango especificado
primos_en_rango = numeros_primos_en_rango(inicio, fin)
if primos_en_rango:
    print("Números primos en el rango:", primos_en_rango)
else:
    print("No se encontraron números primos en el rango especificado.")