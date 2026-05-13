print("Ejemplo de manejo de múltiples excepciones")
print( "Intentaremos dividir 10 por un número ingresado por el usuario.")
try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Entrada no válida")