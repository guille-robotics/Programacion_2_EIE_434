import numpy as np
import matplotlib.pyplot as plt

# 1. Vector de tiempo
t = np.linspace(0, 2, 800)

# 2. Señal ideal (Carga de un capacitor / lectura de sensor)
V_ideal = 3.3 * (1 - np.exp(-2 * t))

# 3. Generación de ruido aleatorio (distribución normal)
ruido = np.random.normal(0, 0.2, len(t))

# 4. Señal medida (Suma elemento a elemento)
V_medida = V_ideal + ruido

# 5. Gráfico superpuesto
plt.figure(figsize=(10, 5))

# Primero la señal ruidosa (color tenue)
plt.plot(t, V_medida, color='steelblue', alpha=0.5, label='Señal Medida (con ruido)')

# Luego la señal ideal (color oscuro y línea gruesa)
plt.plot(t, V_ideal, color='black', linewidth=2.5, label='Señal Ideal (filtrada)')

plt.title('Lectura de Sensor Analógico: Señal con Ruido vs Ideal')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()