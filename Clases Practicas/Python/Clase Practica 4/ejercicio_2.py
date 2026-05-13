import pandas as pd

# a) Carga y verificación de propiedades
df = pd.read_csv('calidad_aire.csv')
print("Dimensiones:", df.shape)  # 
print("Tipos de datos:\n", df.dtypes) # 

# b) Resumen estadístico con .describe()
# Esto mostrará media, max, min, etc. de todas las columnas
print("\nResumen Estadístico:")
print(df.describe()) 

# c) Promedio de temperatura
promedio_temp = df['temperatura'].mean() # 
print(f"\nEl promedio de temperatura es: {promedio_temp:.2f}°C")

# d) Filtrado por PM2.5 (Alta contaminación)
# Usamos una máscara booleana como en la Clase 6 
filtro_contaminacion = df[df['pm25'] > 35]
print(f"\nSe encontraron {len(filtro_contaminacion)} registros sobre el umbral.")

# e) Exportación de resultados
# index=False evita que se guarde la columna de números de la izquierda 
filtro_contaminacion.to_csv('alerta_aire.csv', index=False)
print("\nArchivo 'alerta_aire.csv' generado con éxito.")