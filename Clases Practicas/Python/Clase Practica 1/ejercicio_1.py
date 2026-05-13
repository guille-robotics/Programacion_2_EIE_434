# Pedimos al usuario cuántos términos quiere
n = int(input("Ingrese el número de términos: "))

# Verificamos que el número sea válido
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Definimos los dos primeros términos de la serie
    a = 0  # Primer número de Fibonacci
    b = 1  # Segundo número de Fibonacci
    contador = 0  # Contador de términos

    print("Serie de Fibonacci hasta", n, "términos:")

    # Mientras el contador sea menor a n, generamos la serie
    while contador < n:
        print(f"Valor de la Serie {a}\n")
        temp = a + b  # Calculamos el siguiente número
        a = b  # Movemos a la siguiente posición
        b = temp  # Asignamos el nuevo valor a b
        contador += 1  # Aumentamos el contador