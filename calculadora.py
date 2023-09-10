def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b
   

while True:
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Seleccione una operación (1/2/3/4/5): ")
    
    if opcion == '5':
        print("!!!adioooooooooos¡¡¡")
        break
    
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer dijito: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
    else:
        print("ingrese una respuesta valida")