import numpy as np
import matplotlib.pyplot as plt

# 1. Vector de tiempo
t = np.linspace(0, 0.2, 1000)

# 2. Señal moduladora (baja frecuencia) y portadora (alta frecuencia)
m_t = np.cos(2 * np.pi * 5 * t)
c_t = np.sin(2 * np.pi * 100 * t)

# 3. Señal modulada AM
s_t = (1 + 0.8 * m_t) * c_t

# 4 y 5. Gráfico de ambas señales superpuestas
plt.figure(figsize=(10, 5))

# Graficamos la modulada primero
plt.plot(t, s_t, 'b-', label='Señal Modulada s(t)')

# Graficamos la moduladora como "envolvente" (línea punteada roja y gruesa)
plt.plot(t, m_t, 'r--', linewidth=2.5, label='Señal Moduladora m(t)')


plt.title('Modulación de Amplitud (AM)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()