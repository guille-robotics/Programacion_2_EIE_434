import time

datos_sensor = [10, 20, 30]
configuracion = {"modo": "auto"}

try:
    print("Iniciando programa...")
    # Descomenta UNA linea a la vez para probar cada error:
    
    # x = 10 / 0                      # 1. ZeroDivisionError
    # y = int("falla")                # 2. ValueError
    # z = "Sensor " + 5               # 3. TypeError
    # val = datos_sensor[5]           # 4. IndexError
    # est = configuracion["vel"]      # 5. KeyError
    #time.sleep(10)                  # 6. KeyboardInterrupt (Presiona Ctrl+C)

except ZeroDivisionError:
    print("Error: Intento de division por cero.")
except ValueError:
    print("Error: Valor incorrecto para la conversion.")
except TypeError:
    print("Error: Operacion entre tipos de datos incompatibles.")
except IndexError:
    print("Error: Indice fuera de los limites de la lista.")
except KeyError:
    print("Error: Clave no encontrada en el diccionario.")
except KeyboardInterrupt:
    print("\nEjecucion detenida forzosamente por el usuario.")