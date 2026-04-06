import pandas as pd

# 1. Cargar los datos desde el archivo CSV
df_notas = pd.read_csv("notas_alumnos.csv")

# 2. Limpiar las filas que contienen valores nulos (NaN)
df_limpio = df_notas.dropna()

# 3. Generar la nueva columna calculando el promedio
df_limpio["Promedio"] = (df_limpio["Parcial_1"] + df_limpio["Parcial_2"]) / 2

# 4. Mostrar el registro final
print("=== Registro de Notas Oficial ===")
print(df_limpio)