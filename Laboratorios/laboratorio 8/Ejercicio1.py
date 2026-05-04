import numpy as np
import matplotlib.pyplot as plt

# 1. Crear vector de tiempo
t = np.linspace(0, 10, 100)

# 2. Calcular la señal (seno)
y = np.sin(t)

# 3. Graficar
plt.plot(t, y, color='blue')
plt.title("Lectura de Sensor (Señal Senoidal)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()