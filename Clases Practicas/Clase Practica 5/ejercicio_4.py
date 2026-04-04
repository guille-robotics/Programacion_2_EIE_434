# Forma tradicional con try-except-finally
archivo = None
try:
    # Intenta cambiar el nombre para probar el FileNotFoundError
    archivo = open('parametros_robot.txt', 'r')  # Luego de probar el error, asegúrate de que el archivo exista o crea uno vacío con ese nombre.
    print("Archivo abierto correctamente.")
    
    # Error forzado
    fallo = 10 / 0 

except FileNotFoundError:
    print("Archivo de configuración no encontrado.")
except ZeroDivisionError:
    print("Error de cálculo durante la lectura del archivo.")
finally:
    if archivo is not None:
        archivo.close()
        print("El archivo ha sido cerrado de forma segura en el bloque finally.")
    else:
        print("Finalizando ejecución (no había archivo que cerrar).")

print("-" * 30)

# Opcional: Forma moderna con 'with'
''' 
try:
    with open('parametros_robot.txt', 'r') as archivo_with:
        print("Archivo abierto con 'with'.")
        fallo_2 = 10 / 0
except FileNotFoundError:
    print("Archivo no encontrado (usando with).")
except ZeroDivisionError:
    print("Error de cálculo (el archivo se cerró solo gracias al with).")

'''
