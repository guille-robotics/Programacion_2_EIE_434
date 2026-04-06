import pandas as pd

datos_juegos = {
    "Juego": ["Cyberpunk 2077", "Minecraft", "Hollow Knight", "FIFA 24"],
    "Precio_Base": [40000, 15000, 7500, 45000],
    "Descuento_Porcentaje": [50, 0, 20, 10]
}
df_juegos = pd.DataFrame(datos_juegos)

# 1. Calcular el Precio Final usando operaciones vectorizadas
descuento = df_juegos["Precio_Base"] * (df_juegos["Descuento_Porcentaje"] / 100)
df_juegos["Precio_Final"] = df_juegos["Precio_Base"] - descuento

# 2. Crear filtro para juegos a menos de 20.000 CLP
filtro_oferta = df_juegos["Precio_Final"] < 20000
df_ofertas = df_juegos[filtro_oferta]

# 3. Imprimir el resultado
print("=== Videojuegos en Oferta (Menos de $20.000) ===")
print(df_ofertas)