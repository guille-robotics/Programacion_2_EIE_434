import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
R = 1000  # Resistencia en ohmios
C = 0.001  # Capacitancia en faradios
V_max = 5  # Voltaje máximo (V) durante la carga
V_inicial = 5  # Vo durante la descarga (V)

# Tiempo
t = np.linspace(0, 5 * R * C, 1000)  # T de 0 a 5 (RC)

# Curva de carga (Voltaje en función del tiempo)
V_carga = V_max * (1 - np.exp(-t / (R * C)))

# Curva de descarga (Voltaje en función del tiempo)
V_descarga = V_inicial * np.exp(-t / (R * C))

# Graficar las curvas
plt.figure(figsize=(10, 6))
plt.plot(t, V_carga, label="Carga del Capacitor", color='b')
plt.plot(t, V_descarga, label="Descarga del Capacitor", color='r')
plt.title("Curvas de Carga y Descarga de un Capacitor")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid(True)
plt.show()