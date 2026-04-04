import pandas as pd 
import matplotlib.pyplot as plt 

# a) Carga y limpieza 
df = pd.read_csv('sensor_datos.csv')
df = df.dropna()  # Elimina filas con nulos 

# b) Nueva columna Potencia (P = V * I) 
df['Potencia_W'] = df['voltaje'] * df['corriente'] 

# c) Columna booleana de alerta 
df['Alerta_Humedad'] = df['humedad'] > 70

# d) Gráfico comparativo 
plt.figure(figsize=(10, 5)) 
plt.plot(df['fecha'], df['temperatura'], 'o-', label='Temperatura (°C)', color='blue') 
plt.plot(df['fecha'], df['Potencia_W'], 's-', label='Potencia (W)', color='red') 

# e) Estética y legibilidad 
plt.grid(True, linestyle='--', alpha=0.6) 
plt.xticks(rotation=90)  # Rotación para evitar traslape 
plt.legend() 
plt.title('Relación Temperatura vs. Potencia') 
plt.show() 