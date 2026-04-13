def calcular_promedio_sensor():
    # Base de datos simulada en memoria
    sensores = {
        'temp': [22.5, 23.1, 22.8], 
        'presion': [1013, 1015], 
        'humedad': []
    }
    
    nombre_sensor = input("Ingrese el nombre del sensor a consultar ('temp', 'presion', 'humedad'): ")
    
    try:
        # Intentamos acceder a la llave del diccionario
        lecturas = sensores[nombre_sensor]
        
        # Intentamos calcular el promedio (sum / cantidad)
        promedio = sum(lecturas) / len(lecturas)
        print(f"El promedio de las lecturas del sensor '{nombre_sensor}' es: {promedio:.2f}")
        
    except KeyError:
        # Se activa si la llave solicitada no existe en el diccionario
        print(f"Error crítico: El sensor '{nombre_sensor}' no se encuentra registrado en el sistema.")
        
    except ZeroDivisionError:
        # Se activa si len(lecturas) es 0
        print(f"Advertencia: El sensor '{nombre_sensor}' no tiene lecturas registradas (división por cero evitada).")
        
    finally:
        # Ejecución garantizada, ideal para cerrar conexiones a bases de datos o finalizar procesos
        print("Consulta de sensor finalizada.\n")

# Pruebas interactivas
# Si el alumno ingresa 'temp' -> Imprime promedio
# Si el alumno ingresa 'humedad' -> Gatilla ZeroDivisionError
# Si el alumno ingresa 'voltaje' -> Gatilla KeyError
if __name__ == "__main__":
    calcular_promedio_sensor()