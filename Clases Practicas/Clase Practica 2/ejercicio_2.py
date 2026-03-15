# Diccionario con información de los dispositivos de red
# Cada clave es el nombre del dispositivo
# Cada valor es OTRO diccionario con sus características
dispositivos = {
    "Router_1": {"ip": "192.168.1.1", "estado": "activo", "trafico_mbps": 120},
    "Switch_1": {"ip": "192.168.1.2", "estado": "activo", "trafico_mbps": 80},
    "AP_1": {"ip": "192.168.1.3", "estado": "inactivo", "trafico_mbps": 0},
    "Servidor_1": {"ip": "192.168.1.10", "estado": "activo", "trafico_mbps": 250}
}


def contar_activos(red):
    """
    Cuenta cuántos dispositivos están en estado activo.
    """
    contador = 0  # acumulador

    for nombre in red:  # recorre las claves del diccionario
        # red[nombre] es el diccionario interno del dispositivo
        if red[nombre]["estado"] == "activo":  # accedemos al campo "estado"
            contador += 1  # aumentamos el contador

    return contador  # retornamos el total


def trafico_total(red):
    """
    Suma el tráfico total de todos los dispositivos.
    """
    total = 0  # acumulador

    for nombre in red:
        # sumamos el tráfico de cada dispositivo
        total += red[nombre]["trafico_mbps"]

    return total


def buscar_inactivos(red):
    """
    Retorna una lista con los nombres de los dispositivos inactivos.
    """
    inactivos = []  # lista vacía para guardar resultados

    for nombre in red:
        if red[nombre]["estado"] == "inactivo":
            inactivos.append(nombre)  # guardamos solo el nombre (la clave)

    return inactivos


def mayor_trafico(red):
    """
    Retorna el nombre del dispositivo con mayor tráfico
    y el valor de tráfico correspondiente.
    """
    nombres = list(red.keys())  # obtenemos una lista de claves

    # Importante: se necesita un valor inicial para comparar
    # Tomamos el primer elemento como referencia
    nombre_mayor = nombres[0]
    trafico_mayor = red[nombre_mayor]["trafico_mbps"]

    for nombre in red:
        # comparamos el tráfico actual con el máximo encontrado
        if red[nombre]["trafico_mbps"] > trafico_mayor:
            trafico_mayor = red[nombre]["trafico_mbps"]
            nombre_mayor = nombre  # actualizamos el nombre

    return nombre_mayor, trafico_mayor  # retornamos ambos valores


# ================== PROGRAMA PRINCIPAL ==================

# Llamadas a las funciones (procesamiento de datos)
cantidad_activos = contar_activos(dispositivos)
total_trafico = trafico_total(dispositivos)
lista_inactivos = buscar_inactivos(dispositivos)
equipo_mayor, trafico_mayor = mayor_trafico(dispositivos)

# Mostramos resultados (salida por pantalla)
print("=== Análisis de la Red ===")
print(f"Cantidad de dispositivos activos: {cantidad_activos}")
print(f"Tráfico total de la red: {total_trafico} Mbps")
print(f"Dispositivos inactivos: {lista_inactivos}")
print(f"Dispositivo con mayor tráfico: {equipo_mayor} ({trafico_mayor} Mbps)")