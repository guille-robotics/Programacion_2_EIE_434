def convertir_a_celsius(fahrenheit):
    try:
        # Verificamos si el valor es numérico
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError("Entrada no válida. Por favor ingresa un número")
        
        # Comprobamos si la temperatura es negativa
        if fahrenheit < 0:
            raise ValueError("La temperatura no puede ser negativa")
        
        # Realizamos la conversión
        celsius = (5/9) * (fahrenheit - 32)
        return celsius
    except ValueError as e:
        return str(e)
    

# Probar la función con diferentes casos
print(convertir_a_celsius(98.6))
print(convertir_a_celsius("abc"))
print(convertir_a_celsius(-10)) 