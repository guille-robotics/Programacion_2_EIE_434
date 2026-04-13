def procesar_trama(trama):
    try:
        # Intentamos separar el ID del valor
        partes = trama.split(":") 
        id_sensor = partes[0]
        valor = float(partes[1])
        print(f"Sensor {id_sensor} operativo: {valor} unidades.")
        
    except IndexError:
        # Ocurre si el split no encuentra el ":"
        print("Error: Trama mal formateada (falta delimitador ':').")
    except ValueError:
        # Ocurre si el valor no se puede convertir a float (ej: 'abc')
        print("Error: El valor recibido no es numérico.")
    except Exception as e:
        # Captura cualquier otro error (jerarquía genérica siempre al final)
        print(f"Ocurrió un error inesperado: {e}")

# Pruebas
procesar_trama("TEMP:25.4")  # Correcto
procesar_trama("HUM_40")      # Gatilla IndexError
procesar_trama("PRES:N/A")    # Gatilla ValueError