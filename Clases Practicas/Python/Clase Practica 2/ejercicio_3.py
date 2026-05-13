import math  # librería matemática para usar sqrt()

# Lista de cargas trifásicas
# Cada elemento de la lista es un diccionario que representa una carga
cargas = [
    {"nombre": "Motor_1", "voltaje": 400, "corriente": 12, "fp": 0.86},
    {"nombre": "Bomba_1", "voltaje": 400, "corriente": 8, "fp": 0.82},
    {"nombre": "Compresor_1", "voltaje": 400, "corriente": 15, "fp": 0.90},
    {"nombre": "Ventilador_1", "voltaje": 400, "corriente": 5, "fp": 0.78}
]


def calcular_potencia(voltaje, corriente, fp):
    """
    Calcula la potencia activa trifásica usando:
    P = sqrt(3) * V * I * fp
    """
    # Importante: math.sqrt(3) representa √3 en Python
    potencia = math.sqrt(3) * voltaje * corriente * fp
    return potencia


def procesar_cargas(lista_cargas):
    """
    Recorre la lista de cargas, calcula la potencia de cada una
    y agrega ese valor al diccionario correspondiente.
    """
    for carga in lista_cargas:
        # 'carga' es un diccionario individual dentro de la lista
        potencia = calcular_potencia(
            carga["voltaje"],   # acceso al valor de voltaje
            carga["corriente"], # acceso a la corriente
            carga["fp"]         # acceso al factor de potencia
        )

        # Importante: aquí estamos AGREGANDO una nueva clave al diccionario
        carga["potencia"] = potencia

    return lista_cargas  # retornamos la lista modificada


def resumen_cargas(lista_cargas):
    """
    Retorna:
    - potencia total
    - nombre de la carga de mayor potencia
    - lista de cargas con factor de potencia menor a 0.80
    """
    potencia_total = 0  # acumulador
    cargas_fp_bajo = []  # lista para guardar resultados

    # Importante: inicialización para buscar el máximo
    # Se usa el primer elemento como referencia inicial
    nombre_mayor = lista_cargas[0]["nombre"]
    potencia_mayor = lista_cargas[0]["potencia"]

    for carga in lista_cargas:
        # sumamos la potencia de cada carga
        potencia_total += carga["potencia"]

        # buscamos la carga con mayor potencia
        if carga["potencia"] > potencia_mayor:
            potencia_mayor = carga["potencia"]
            nombre_mayor = carga["nombre"]

        # filtramos cargas con bajo factor de potencia
        if carga["fp"] < 0.80:
            cargas_fp_bajo.append(carga["nombre"])

    return potencia_total, nombre_mayor, cargas_fp_bajo


# ================== PROGRAMA PRINCIPAL ==================

# Procesamos las cargas para calcular y agregar la potencia
cargas_actualizadas = procesar_cargas(cargas)

# Obtenemos el resumen general (análisis de datos)
pot_total, carga_mayor, lista_fp_bajo = resumen_cargas(cargas_actualizadas)

# Mostramos el reporte (salida de información)
print("=== Reporte de Cargas Trifásicas ===")

for carga in cargas_actualizadas:
    # recorremos la lista y mostramos cada diccionario
    print(f"Carga: {carga['nombre']}")
    print(f"  Voltaje: {carga['voltaje']} V")
    print(f"  Corriente: {carga['corriente']} A")
    print(f"  Factor de potencia: {carga['fp']}")
    print(f"  Potencia activa: {carga['potencia']:.2f} W")  # formateo a 2 decimales
    print()

# resultados finales
print(f"Potencia total consumida: {pot_total:.2f} W")
print(f"Carga de mayor potencia: {carga_mayor}")
print(f"Cargas con factor de potencia menor a 0.80: {lista_fp_bajo}")