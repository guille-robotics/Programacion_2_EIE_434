import pandas as pd

# Diccionario inicial
datos = {
    "Componente": ["Arduino", "Resistencia 1k", "Capacitor", "Motor DC"],
    "Stock": [5, 500, 120, 3]
}

# 1. Crear el DataFrame
df = pd.DataFrame(datos)

# 2. Filtrar stock crítico (menor a 10)
df_critico = df[df["Stock"] < 10]

# 3. Imprimir el resultado
print("--- Componentes con Stock Crítico ---")
print(df_critico)