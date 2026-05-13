# Diccionario con información de una flota de robots
# Cada clave es el nombre del robot
# Cada valor es un diccionario con IP, estado y precio
flota_robots = {
    "Brazo_Soldador_1": {"ip": "10.10.5.1", "estado": "activo", "precio": 55},
    "Brazo_Soldador_2": {"ip": "10.10.5.2", "estado": "mantenimiento", "precio": 28},
    "AGV_Transporte_1": {"ip": "10.10.5.3", "estado": "activo", "precio": 38},
    "AGV_Transporte_2": {"ip": "10.10.5.4", "estado": "activo", "precio": 42},
    "Dron_Inspector_1": {"ip": "10.10.5.5", "estado": "inactivo", "precio": 22},
    "Robot_Ensamblador_1": {"ip": "10.10.5.10", "estado": "activo", "precio": 45},
    "Robot_Ensamblador_2": {"ip": "10.10.5.11", "estado": "mantenimiento", "precio": 75},
    "Robot_Pintura_1": {"ip": "10.10.5.20", "estado": "activo", "precio": 36}
}

# items() permite ver pares clave-valor (nombre, datos)
#print(flota_robots.items())


def estadisticas_flota(flota):
    # Acumulador del precio total
    precio_total = 0

    # Contadores por estado
    activos = 0
    mantenimiento = 0
    inactivos = 0

    # Listas para almacenar IPs según estado
    activos_list = []
    mantenimiento_list = []
    inactivos_list = []

    # Lista para robots con precio alto
    caros = []

    # Recorremos el diccionario usando .items()
    # nombre = clave (ej: "AGV_Transporte_1")
    # datos = diccionario interno
    for nombre, datos in flota.items():

        # Extraemos los valores del diccionario interno
        precio = datos["precio"]
        estado = datos["estado"]
        ip = datos["ip"]

        # Sumamos el precio total (acumulador)
        precio_total += precio

        # Clasificación según estado del robot
        if estado == "activo":
            activos += 1
            activos_list.append(ip)  # guardamos la IP

        elif estado == "mantenimiento":
            mantenimiento += 1
            mantenimiento_list.append(ip)

        else:
            # Cualquier otro estado se considera inactivo
            inactivos += 1
            inactivos_list.append(ip)

        # Filtrado: robots con precio mayor a 30
        if precio > 30:
            caros.append(nombre)  # guardamos el nombre del robot

    # Retornamos múltiples resultados
    return precio_total, activos, mantenimiento, inactivos, activos_list, mantenimiento_list, inactivos_list, caros


# ================== PROGRAMA PRINCIPAL ==================

# Llamada a la función
precio_total, activos, mantenimiento, inactivos, activos_list, mantenimiento_list, inactivos_list, caros = estadisticas_flota(flota_robots)

# Mostramos resultados
print("---- Estadísticas de la flota de Robots ----")
print("Precio Total:", precio_total)
print("------------------------------------------")
print("Activos:", activos, "IPs:", activos_list)
print("En mantenimiento:", mantenimiento, "IPs:", mantenimiento_list)
print("Inactivos:", inactivos, "IPs:", inactivos_list)
print("------------------------------------------")
print("Robots con precio mayor a 30:", caros)