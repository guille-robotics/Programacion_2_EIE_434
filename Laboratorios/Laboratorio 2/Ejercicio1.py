# Definición de la red de nodos ESP8266
red_esp8266 = {
    "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
    "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
    "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
    "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000}
}

def auditar_red(nodos):
    total_nodos = len(nodos)
    ips_problema = []
    suma_dac = 0
    nodos_activos = 0
    
    # Recorremos el diccionario usando items()
    for nombre, datos in nodos.items():
        if datos["estado"] in ["falla", "inactivo"]:
            ips_problema.append(datos["ip"])
        elif datos["estado"] == "activo":
            suma_dac += datos["salida_dac"]
            nodos_activos += 1
            
    # Calculamos el promedio evitando división por cero
    promedio_dac = suma_dac / nodos_activos if nodos_activos > 0 else 0
    
    return total_nodos, ips_problema, promedio_dac

# Llamada a la función y desempaquetado de retornos
total, ips_revision, promedio = auditar_red(red_esp8266)

# Impresión de resultados
print(f"Total de nodos registrados: {total}")
print(f"IPs que requieren revisión (falla/inactivo): {ips_revision}")
print(f"Promedio de salida DAC (nodos activos): {promedio:.2f}")