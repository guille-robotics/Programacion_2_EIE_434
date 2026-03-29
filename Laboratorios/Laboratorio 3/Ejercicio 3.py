import random
import time
import numpy as np

# Tamaño de las matrices
N = 100

# 1. Crear matrices en Python clásico (listas anidadas)
A_list = [[random.random() for _ in range(N)] for _ in range(N)]
B_list = [[random.random() for _ in range(N)] for _ in range(N)]

# 2. Crear equivalentes en NumPy
A_np = np.array(A_list)
B_np = np.array(B_list)

# 3. Multiplicación clásica (3 ciclos for anidados)
inicio_py = time.time()
C_list = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            C_list[i][j] += A_list[i][k] * B_list[k][j]
fin_py = time.time()
tiempo_py = fin_py - inicio_py

# 4. Multiplicación con NumPy
inicio_np = time.time()
# Se puede usar np.dot(A_np, B_np) o el operador @
C_np = A_np @ B_np 
fin_np = time.time()
tiempo_np = fin_np - inicio_np

# 5. Imprimir resultados y comparación
print(f"Tiempo de ejecución Python clásico: {tiempo_py:.4f} segundos")
print(f"Tiempo de ejecución NumPy: {tiempo_np:.6f} segundos")

if tiempo_np > 0:
    print(f"NumPy fue {tiempo_py / tiempo_np:.2f} veces más rápido.")