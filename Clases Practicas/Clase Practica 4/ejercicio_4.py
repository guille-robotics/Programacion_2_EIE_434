import pandas as pd 
import matplotlib.pyplot as plt 

# a) Carga y eliminación de duplicados
df = pd.read_csv('motor_dc.csv')
df = df.drop_duplicates()

# b) Rellenar nulos con el promedio (fillna) 
promedio_temp = df['temperatura_motor'].mean() 
df['temperatura_motor'] = df['temperatura_motor'].fillna(promedio_temp) 

# c) Filtrado de fallas (Bloqueo del motor) [cite: 307]
falla = df[(df['velocidad_rpm'] < 100) & (df['corriente_a'] > 5.0)] # 5.0 como ejemplo nominal

# d) Gráfico de temperatura [cite: 376, 417]
plt.plot(df['tiempo_s'], df['temperatura_motor'], color='orange')
plt.xlabel('Tiempo (s)') 
plt.ylabel('Temperatura (°C)') 
plt.title('Monitoreo Térmico del Motor') 

# e) Ajuste automático de márgenes [cite: 480]
plt.tight_layout() # Evita cortes en etiquetas [cite: 482]
plt.show()