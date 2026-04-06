import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo de ventas
df_ventas = pd.read_csv("ventas_tienda.csv")

# 2 y 3. Configurar el lienzo y graficar ambas líneas
plt.figure(figsize=(9, 5))

plt.plot(df_ventas["Mes"], df_ventas["Laptops"], 
         color="blue", marker="o", label="Laptops")

plt.plot(df_ventas["Mes"], df_ventas["Smartphones"], 
         color="green", marker="s", label="Smartphones")

# 4. Añadir títulos, etiquetas y leyenda
plt.title("Evolución de Ventas Mensuales")
plt.xlabel("Mes del Año")
plt.ylabel("Unidades Vendidas")
plt.legend() # Muestra el cuadro que identifica los colores

# 5. Activar la grilla y mostrar en pantalla
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout() # Ajusta automáticamente los márgenes
plt.show()