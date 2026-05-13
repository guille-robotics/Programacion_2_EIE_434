import pandas as pd

# 1. Cargar y Limpiar
df = pd.read_csv('sensores_brutos.csv')
df = df.dropna()

# 2. Operación (Columna Derivada)
# Supongamos que ya tienen Potencia o la calculan
df['Potencia (W)'] = df['Voltaje (V)'] * df['Corriente (A)']
df['Energia_Wh'] = df['Potencia (W)'] * 1 

# 3. Filtrado
df_filtrado = df[df['Humedad (%)'] < 60]

# 4. Exportación
df_filtrado.to_csv('datos_limpios_EIE434.csv', index=False)