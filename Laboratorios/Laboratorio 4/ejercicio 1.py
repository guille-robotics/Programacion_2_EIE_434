import pandas as pd

# 1 y 2. Crear el diccionario con las canciones
datos_playlist = {
    "Cancion": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine"],
    "Artista": ["Queen", "Led Zeppelin", "Eagles", "John Lennon"],
    "Duracion_seg": [354, 482, 390, 183]
}

# 3. Convertir el diccionario a un DataFrame
df_playlist = pd.DataFrame(datos_playlist)

# 4. Mostrar propiedades estructurales
print("Dimensiones del DataFrame (filas, columnas):", df_playlist.shape)
print("\nTipos de datos de las columnas:")
print(df_playlist.dtypes)