# Pedimos al usuario un número entero positivo
n = int(input("Ingrese el número de términos: "))

# Validamos que el número sea positivo
while n <= 0:
    print("Error: Debe ingresar un número entero positivo.")
    n = int(input("Ingrese el número de términos: "))  # Pedimos el número nuevamente

# Calculamos y mostramos los factoriales
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f"Factorial de {i} es {factorial}")