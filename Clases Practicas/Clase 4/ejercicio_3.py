import pandas as pd
import matplotlib.pyplot as plt

# a) Carga y Slicing con iloc 
df = pd.read_csv('consumo_energia.csv')
print("Filas 5 a 15:")
print(df.iloc[5:16]) # El límite superior no se incluye 

# b) Cálculo de Correlación 

""" 
¿Qué es la Correlación en Pandas?
La correlación indica qué tan "conectadas"
están dos variables. En términos simples: si una sube, ¿la otra también sube, baja o no le pasa nada?
En Pandas usamos el método .corr():
Valor cercano a 1: Correlación positiva fuerte. Si el consumo sube, el costo sube (lo lógico en este ejercicio).
Valor cercano a 0: No hay relación lineal. Las variables son independientes.
Valor cercano a -1: Correlación negativa fuerte. Si una sube, la otra baja.
"""
# Este valor nos dice qué tan ligados están el consumo y el precio
coeficiente = df['consumo_kwh'].corr(df['costo_clp'])
print(f"\nCoeficiente de Correlación: {coeficiente:.4f}")

# c) Filtrado por promedio (Días de ahorro) 
promedio_consumo = df['consumo_kwh'].mean()
df_ahorro = df[df['consumo_kwh'] < promedio_consumo]
print(f"Días de ahorro detectados: {len(df_ahorro)}")

# d) Gráfico personalizado 
plt.figure(figsize=(10, 5))
plt.plot(df['fecha'], df['consumo_kwh'], color='green', marker='x', linestyle='-', label='Consumo (kWh)')
plt.title('Historial de Consumo Energético')
plt.xlabel('Fecha') 
plt.ylabel('kWh') 
plt.xticks(rotation=90) 
plt.grid(True, alpha=0.3)
plt.legend() 
plt.tight_layout() 
plt.show()

# e) Exportación a JSON 
df_ahorro.to_json('ahorro_energetico.json', indent=4)
print("\nArchivo JSON exportado correctamente.")