import numpy as np

# Matriz de transformación de la base del robot a la mesa
T_base_mesa = np.array([
    [1, 0, 0, 2],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Matriz de transformación de la mesa al objeto
T_mesa_objeto = np.array([
    [1, 0, 0, 0.5],
    [0, 1, 0, 0.3],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Multiplicación de matrices
T_base_objeto = T_base_mesa @ T_mesa_objeto

# Extraer la posición del objeto
x = T_base_objeto[0, 3]
y = T_base_objeto[1, 3]
z = T_base_objeto[2, 3]

print("Matriz base a objeto:")
print(T_base_objeto)

print("\nPosición del objeto respecto a la base del robot:")
print("x =", x)
print("y =", y)
print("z =", z)