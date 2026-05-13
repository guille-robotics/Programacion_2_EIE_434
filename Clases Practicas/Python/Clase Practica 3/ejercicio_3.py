import numpy as np
import matplotlib.pyplot as plt

# 1. Array de tiempo (para 3 ciclos de 50 Hz)
t = np.linspace(0, 0.06, 600)

# 2. Generación de las tres fases (Desfasadas 120 grados)
V_pico = 311
f = 50
omega = 2 * np.pi * f

Va = V_pico * np.sin(omega * t)
Vb = V_pico * np.sin(omega * t - (2 * np.pi / 3))
Vc = V_pico * np.sin(omega * t + (2 * np.pi / 3))

# 3. Crear figura principal
plt.figure(figsize=(14, 5))

# 4. Primer subplot (1 fila, 2 columnas, posición 1)
plt.subplot(1, 2, 1)
plt.plot(t, Va, color='red', label='Fase A')
plt.plot(t, Vb, color='blue', label='Fase B')
plt.plot(t, Vc, color='green', label='Fase C')
plt.title('Voltajes Trifásicos en el Tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.legend()
plt.grid(True)

# 5. Segundo subplot (1 fila, 2 columnas, posición 2)
suma_fases = Va + Vb + Vc
plt.subplot(1, 2, 2)
plt.plot(t, suma_fases, color='black', label='Va + Vb + Vc')
plt.title('Suma de las fases (Corriente/Voltaje en el Neutro)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.ylim(-50, 50) # Escala forzada para notar que la suma es ~0
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()