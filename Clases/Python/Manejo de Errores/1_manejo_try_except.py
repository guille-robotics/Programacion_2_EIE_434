# Probamos que sucede cuando se divide entre 0
divisor= int(input("Ingrese el divisor: "))
dividendo= int(input("Ingrese el dividendo: "))
try:
    resultado= dividendo/divisor
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0.")