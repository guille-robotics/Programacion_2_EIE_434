import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el array de tiempo
t = np.linspace(0, 10, 500)

# 2. Generar la matriz de posiciones (3 filas, 500 columnas)
posiciones = np.zeros((3, 500))
posiciones[0, :] = 2 * np.sin(t)  # x(t)
posiciones[1, :] = 2 * np.cos(t)  # y(t)
posiciones[2, :] = 0.5 * t        # z(t)

# 3. Extracción por slicing
x = posiciones[0, :]
y = posiciones[1, :]
z = posiciones[2, :]

# 4. Crear figura y usar plt.subplot(filas, columnas, índice)
plt.figure(figsize=(8, 10))

# Gráfico X (Posición 1)
plt.subplot(3, 1, 1)
plt.plot(t, x, color='red')
plt.title('Coordenada X: x(t) = 2*sin(t)')
plt.ylabel('Posición [m]')
plt.grid(True)

# Gráfico Y (Posición 2)
plt.subplot(3, 1, 2)
plt.plot(t, y, color='blue')
plt.title('Coordenada Y: y(t) = 2*cos(t)')
plt.ylabel('Posición [m]')
plt.grid(True)

# Gráfico Z (Posición 3)
plt.subplot(3, 1, 3)
plt.plot(t, z, color='green')
plt.title('Coordenada Z: z(t) = 0.5*t')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m]')
plt.grid(True)

# Ajustar el espaciado para que no se superpongan los textos
plt.tight_layout()
plt.show()