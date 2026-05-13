n = int(input("Ingrese el número de términos: "))

if n <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"Factorial de {i} es {factorial}")