def calcular_eficiencia(p_salida, p_entrada):
    # Aserción para validar datos lógicos
    try:
        assert (p_salida >= 0 and p_entrada >= 0), "Las potencias no pueden ser negativas"
        eficiencia = (p_salida / p_entrada) * 100
        return f"Eficiencia: {eficiencia}%"
    except ZeroDivisionError:
        return "Error: Motor apagado o sin consumo (División por cero)."
    except AssertionError as e:
        return e

# Pruebas
print(calcular_eficiencia(-50, 100))
print(calcular_eficiencia(150, 200))
print(calcular_eficiencia(100, 0))
 
