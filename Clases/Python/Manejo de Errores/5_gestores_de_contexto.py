# Forma tradicional (requiere finally)
archivo = open('registro_datos.txt', 'r')
try:
    contenido = archivo.read()
finally:
    archivo.close() # Siempre debemos recordar cerrar

# Forma recomendada usando 'with'
'''with open('registro_datos.txt', 'r') as archivo:
    contenido = archivo.read()
    # El archivo se cierra automaticamente al salir del bloque
    # No necesitamos try-finally para esto'''