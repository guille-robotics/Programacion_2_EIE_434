import random
import time
import numpy as np

# Cantidad de elementos
elementos = 5000000

# 1. Crear lista clásica en Python
lista_py = [random.random() for _ in range(elementos)]

# 2. Crear arreglo equivalente en NumPy 
# (Usamos los mismos datos para que la comparación sea justa)
arr_np = np.array(lista_py)

# 3. Calcular cuadrados con Python (List Comprehension)
inicio_py = time.time()
cuadrados_py = [x**2 for x in lista_py]
fin_py = time.time()
tiempo_py = fin_py - inicio_py

# 4. Calcular cuadrados con NumPy (Vectorización masiva)
inicio_np = time.time()
cuadrados_np = arr_np ** 2
fin_np = time.time()
tiempo_np = fin_np - inicio_np

# 5. Imprimir resultados y comparación
print(f"Tiempo Python (List Comprehension): {tiempo_py:.4f} segundos")
print(f"Tiempo NumPy (Vectorización): {tiempo_np:.6f} segundos")

if tiempo_np > 0:
    print(f"NumPy fue {tiempo_py / tiempo_np:.2f} veces más rápido.")