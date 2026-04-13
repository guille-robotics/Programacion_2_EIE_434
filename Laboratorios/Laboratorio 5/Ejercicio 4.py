import math

def calcular_impedancia():
    print("--- Calculadora de Impedancia |Z| ---")
    try:
        # Solicitamos los datos al usuario
        r_str = input("Ingrese la Resistencia (R) en Ohmios: ")
        x_str = input("Ingrese la Reactancia (X) en Ohmios: ")

        # Intentamos la conversión
        r = float(r_str)
        x = float(x_str)

        # Cálculo matemático
        z = math.sqrt(r**2 + x**2)

    except ValueError:
        print("Error: Se han detectado caracteres inválidos. Debe ingresar valores numéricos.")
    else:
        # El bloque else solo se ejecuta si el bloque try terminó sin lanzar excepciones
        print(f"Cálculo exitoso. La magnitud de la impedancia |Z| es: {z:.2f} Ohmios.")

# Prueba interactiva
if __name__ == "__main__":
    calcular_impedancia()