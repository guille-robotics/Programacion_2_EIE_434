# Diccionario con información de estaciones remotas
# Cada clave es el nombre de la estación
# Cada valor es un diccionario con variables medidas
estaciones = {
    "EST_01": {"temperatura": 42, "voltaje": 48.5, "senal": -67, "enlace": "ok"},
    "EST_02": {"temperatura": 55, "voltaje": 46.8, "senal": -81, "enlace": "ok"},
    "EST_03": {"temperatura": 39, "voltaje": 44.9, "senal": -75, "enlace": "caido"},
    "EST_04": {"temperatura": 61, "voltaje": 47.2, "senal": -88, "enlace": "ok"}
}


def evaluar_estacion(nombre, datos):
    """
    Evalúa una estación remota y determina si está en estado normal o crítico.
    Además, guarda una lista con las fallas detectadas.
    """
    fallas = []  # lista para almacenar las fallas encontradas

    # Revisamos cada condición de falla accediendo a los valores del diccionario
    if datos["temperatura"] > 50:
        fallas.append("Temperatura alta")

    if datos["voltaje"] < 46.0:
        fallas.append("Voltaje bajo")

    if datos["senal"] < -80:
        fallas.append("Señal débil")

    if datos["enlace"] != "ok":
        fallas.append("Enlace caído")

    # Determinamos el estado según la cantidad de fallas
    if len(fallas) == 0:
        estado = "Normal"
    else:
        estado = "Crítica"

    return nombre, estado, fallas  # retornamos múltiples valores


def evaluar_varias_estaciones(**estaciones):
    """
    Recibe un número variable de estaciones usando **kwargs.
    Retorna un diccionario resumen con el estado de cada estación.
    """
    resumen = {}

    # estaciones.items() permite recorrer clave (nombre) y valor (datos)
    for nombre, datos in estaciones.items():
        # reutilizamos la función anterior para cada estación
        nombre_estacion, estado, fallas = evaluar_estacion(nombre, datos)

        # construimos un nuevo diccionario con la información procesada
        resumen[nombre_estacion] = {
            "estado": estado,
            "fallas": fallas
        }

    return resumen


def generar_reporte(resumen):
    """
    Muestra un reporte final con:
    - estado de cada estación
    - cantidad de estaciones críticas
    - estación con más fallas detectadas
    """
    cantidad_criticas = 0  # acumulador

    # Inicialización para búsqueda de máximo (estación con más fallas)
    nombres = list(resumen.keys())
    estacion_mas_fallas = nombres[0]
    max_fallas = len(resumen[estacion_mas_fallas]["fallas"])

    print("=== Reporte de Estaciones Remotas ===")

    for nombre in resumen:
        # accedemos a los datos del resumen
        estado = resumen[nombre]["estado"]
        fallas = resumen[nombre]["fallas"]

        print(f"Estación: {nombre}")
        print(f"  Estado: {estado}")
        print(f"  Fallas detectadas: {fallas}")
        print()

        # contamos cuántas estaciones están en estado crítico
        if estado == "Crítica":
            cantidad_criticas += 1

        # buscamos la estación con mayor número de fallas
        if len(fallas) > max_fallas:
            max_fallas = len(fallas)
            estacion_mas_fallas = nombre

    print(f"Cantidad de estaciones críticas: {cantidad_criticas}")
    print(f"Estación con más fallas: {estacion_mas_fallas}")


# ================== PROGRAMA PRINCIPAL ==================

# Evaluamos múltiples estaciones usando **kwargs
# Se pasan como argumentos nombrados (clave=valor)
resumen = evaluar_varias_estaciones(
    EST_01=estaciones["EST_01"],
    EST_02=estaciones["EST_02"],
    EST_03=estaciones["EST_03"],
    EST_04=estaciones["EST_04"]
)

# Generamos el reporte final
generar_reporte(resumen)