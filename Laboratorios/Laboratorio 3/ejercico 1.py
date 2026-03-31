import numpy as np
import matplotlib.pyplot as plt

# 1. Solicitar coeficientes
n = int(input("Ingresa la cantidad de coeficientes para la espiral: "))

# 2. Generar secuencia de Fibonacci (ignoramos el cero inicial para dibujar)
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(8, 8))

# Posición inicial del centro del primer arco y ángulo
cx, cy = 0, 0
angulo = 0

# 3. Dibujar los cuartos de círculo iterativamente
for i in range(n):
    r = fib[i]
    
    # Crear el vector de ángulos para el arco actual (90 grados)
    theta = np.linspace(np.radians(angulo), np.radians(angulo + 90), 100)
    
    # Ecuaciones paramétricas del círculo
    x_arco = cx + r * np.cos(theta)
    y_arco = cy + r * np.sin(theta)
    
    # Dibujar la curva
    ax.plot(x_arco, y_arco, color='blue', lw=2)
    
    # Calcular el centro para la siguiente iteración
    if i < n - 1:
        r_next = fib[i+1]
        angulo_fin = np.radians(angulo + 90)
        # El centro se desplaza empujado por la diferencia de los radios
        cx += (r - r_next) * np.cos(angulo_fin)
        cy += (r - r_next) * np.sin(angulo_fin)
        
    # Girar 90 grados para el próximo arco
    angulo += 90

# 4. Ajustes visuales para mantener las proporciones intactas
ax.set_aspect('equal')
plt.title(f"Espiral de Fibonacci ({n} coeficientes)")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()