import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV
df = pd.read_csv('datos_meteorologicos.csv')

# 2. Inspección inicial
print("--- Primeras filas del DataFrame ---")
print(df.head())
print("\n--- Información de las columnas ---")
print(df.info())

# 3. Gráfico de Variables Eléctricas (Voltaje y Corriente)
plt.figure(figsize=(10, 5))
plt.plot(df['Fecha'], df['Voltaje (V)'], marker='o', label='Voltaje (V)', color='blue')
plt.plot(df['Fecha'], df['Corriente (A)'], marker='s', label='Corriente (A)', color='red')

plt.title('Variables Eléctricas: Voltaje vs Corriente')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 4. Gráfico de Variables Ambientales (Temperatura y Humedad)
plt.figure(figsize=(10, 5))
plt.plot(df['Fecha'], df['Temperatura (°C)'], marker='^', label='Temperatura (°C)', color='orange')
plt.plot(df['Fecha'], df['Humedad (%)'], marker='d', label='Humedad (%)', color='green')

plt.title('Variables Ambientales: Temperatura vs Humedad')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()