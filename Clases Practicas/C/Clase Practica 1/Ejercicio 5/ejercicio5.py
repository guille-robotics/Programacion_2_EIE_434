import time

# 1. Registrar el tiempo de inicio
start_time = time.perf_counter()

# --- CÓDIGO A MEDIR ---
# Ejemplo: El mismo bucle que en C
suma = 0
for i in range(1000000000):
    suma += i
# ----------------------

# 2. Registrar el tiempo de fin
end_time = time.perf_counter()

# 3. Calcular el tiempo transcurrido
time_spent = end_time - start_time

print(f"Resultado de la suma: {suma}")
print(f"Tiempo de ejecución en Python: {time_spent:.6f} segundos")