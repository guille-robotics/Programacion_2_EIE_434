# Solicitar datos al usuario
voltaje = float(input("Ingresa el valor del Voltaje (V): "))
corriente = float(input("Ingresa el valor de la Corriente (A): "))

# Cálculos
resistencia = voltaje / corriente
potencia = voltaje * corriente

# Mostrar resultados básicos
print(f"\nResultados:")
print(f"Resistencia: {resistencia:.2f} Ohmios")
print(f"Potencia disipada: {potencia:.2f} Watts")

# Condicional de seguridad
if potencia > 1000:
    print("¡Peligro! Alta disipación de potencia detectada.")
else:
    print("Operación en rangos seguros.")