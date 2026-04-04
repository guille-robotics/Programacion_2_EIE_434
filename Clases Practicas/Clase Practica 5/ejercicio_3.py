import matplotlib.pyplot as plt

# Diccionario ligeramente expandido para que el gráfico se vea mejor
calibracion = {
    "temp": [1.02, 0.98, 1.04, 1.01], 
    "hum": [1.05, 0.99, 1.02], 
    "presion": [1.0, 0.99, 1.01, 0.98]
}
for nombre, data in calibracion.items():
    print(f"Sensor: {nombre}, Factores de Calibración: {data}") 

try:
    sensor = input("Ingrese el nombre del sensor: ")
    indice = int(input("Ingrese el índice de calibración: "))
    
    # Intentamos acceder al valor solicitado
    valor = calibracion[sensor][indice]
    print(f"El factor de calibración es: {valor}")
    
    # --- INICIO BLOQUE DE PLOTEO ---
    # Si llegamos a esta línea, significa que no hubo errores arriba
    factores = calibracion[sensor]
    indices_x = list(range(len(factores)))
    
    plt.figure(figsize=(7, 5))
    
    # Graficamos todas las barras en un color base (ej. celeste)
    plt.bar(indices_x, factores, color='skyblue', edgecolor='black', label='Otros factores')
    
    # Sobrescribimos la barra seleccionada con otro color para destacarla
    plt.bar(indice, valor, color='orange', edgecolor='black', label='Índice Seleccionado')
    
    # Configuraciones estéticas del gráfico
    plt.title(f"Historial de Calibración - Sensor: {sensor.upper()}")
    plt.xlabel("Índice de registro")
    plt.ylabel("Factor de Calibración")
    plt.xticks(indices_x) # Asegura que el eje X muestre números enteros
    
    # Ajustamos el límite Y para que las barras no choquen con el borde superior
    plt.ylim(0, max(factores) + 0.1) 
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    # Mostramos el gráfico
    plt.show()

# Manejo de excepciones
except KeyError:
    print("Error: El sensor ingresado no existe en el registro.")
except IndexError:
    print("Error: El índice está fuera de rango para ese sensor.")
except ValueError:
    print("Error: El índice debe ser un número entero válido.")