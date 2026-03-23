def evaluar_zona_poligono(x_coords, y_coords):
    # Cálculo de la caja delimitadora (Bounding Box)
    ancho = max(x_coords) - min(x_coords)
    alto = max(y_coords) - min(y_coords)
    
    # Cálculo del área
    area = ancho * alto
    
    # Cálculo del centro geométrico aproximado (punto medio de los extremos)
    centro_x = (max(x_coords) + min(x_coords)) / 2
    centro_y = (max(y_coords) + min(y_coords)) / 2
    centro = (centro_x, centro_y)
    
    return ancho, alto, area, centro

# Listas de prueba según las instrucciones
coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

# Ejecución de la función
ancho, alto, area_total, centro_geom = evaluar_zona_poligono(coords_x, coords_y)

print("--- Análisis de Zona de Seguridad ---")
print(f"Área de la caja delimitadora: {area_total} unidades cuadradas")
print(f"Centro geométrico de la zona: {centro_geom}")