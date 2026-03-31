import matplotlib.pyplot as plt

encuesta = {'Python': 45, 'C++': 28, 'C': 15, 'Java': 12, 'Rust': 8}

# 1. Extraer datos dinámicamente usando un ciclo for
lenguajes = []
votos = []

for lenguaje in encuesta:
    lenguajes.append(lenguaje)               # Guarda el nombre del lenguaje
    votos.append(encuesta[lenguaje])         # Usa el nombre para obtener y guardar el valor

# 2. Crear gráfico de barras y 3. Asignar colores y etiquetas
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(lenguajes, votos, color=colores)

plt.title("Lenguaje de Programación Favorito en la Escuela")
plt.xlabel("Lenguajes")
plt.ylabel("Cantidad de Votos")

# Mostrar gráfico
plt.show()