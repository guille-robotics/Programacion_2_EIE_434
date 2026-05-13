def analizar_consumo(*args, **kwargs):
    """
    Esta función recibe:
    - *args: potencias sin nombre (se almacenan como una tupla)
    - **kwargs: potencias con nombre (se almacenan como un diccionario)

    Retorna:
    - potencia total
    - nombre de la carga de mayor consumo
    """

    potencia_total = 0  # acumulador de todas las potencias

    # Variables para encontrar la carga con mayor consumo
    mayor_valor = 0
    mayor_nombre = "Desconocido"

    # ================== PROCESAMIENTO DE *args ==================
    # args es una tupla: (100, 200, 50, ...)
    for i, valor in enumerate(args):
        potencia_total += valor  # sumamos cada valor

        # Como no tienen nombre, generamos uno automáticamente
        nombre = f"Carga_{i+1}"

        # Comparamos para encontrar el mayor consumo
        if valor > mayor_valor:
            mayor_valor = valor
            mayor_nombre = nombre

    # ================== PROCESAMIENTO DE **kwargs ==================
    # kwargs es un diccionario: {"Motor":300, "Bomba":150, ...}
    for nombre, valor in kwargs.items():
        potencia_total += valor  # sumamos cada valor

        # Aquí ya tenemos nombres reales (Motor, Bomba, etc.)
        if valor > mayor_valor:
            mayor_valor = valor
            mayor_nombre = nombre

    return potencia_total, mayor_nombre  # retornamos ambos resultados


# ================== PROGRAMA PRINCIPAL ==================

# Llamado a la función combinando args y kwargs
total, mayor = analizar_consumo(
    100, 200, 50,      # args (sin nombre)
    Motor=300,         # kwargs (con nombre)
    Bomba=150,
    Compresor=400
)

# Mostramos resultados
print("=== Análisis de Consumo ===")
print(f"Potencia total: {total} W")
print(f"Mayor consumo: {mayor}")