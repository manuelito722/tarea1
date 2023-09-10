def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Calcular y mostrar el factorial
resultado_factorial = factorial(numero)
if isinstance(resultado_factorial, int):
    print(f"El factorial de {numero} es {resultado_factorial}.")
else:
    print(resultado_factorial)