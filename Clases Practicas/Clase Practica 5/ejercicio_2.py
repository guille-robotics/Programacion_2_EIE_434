def calcular_eficiencia(p_salida, p_entrada):
    # Aserción para validar datos lógicos
    assert p_salida >= 0 and p_entrada >= 0, "Las potencias no pueden ser negativas"
    
    try:
        eficiencia = (p_salida / p_entrada) * 100
        return f"Eficiencia: {eficiencia}%"
    except ZeroDivisionError:
        return "Error: Motor apagado o sin consumo (División por cero)."

# Pruebas
print(calcular_eficiencia(150, 200))
print(calcular_eficiencia(100, 0))
#print(calcular_eficiencia(-50, 100)) # Descomentar para ver el AssertionError