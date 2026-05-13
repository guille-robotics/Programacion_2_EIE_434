class Contenido:
    # a) Atributo de clase global
    conteo_total = 0
    
    def __init__(self, titulo, año):
        # Incrementamos el contador global cada vez que nace una instancia
        Contenido.conteo_total += 1
        
        # Atributos de instancia comunes para cualquier tipo de contenido
        self.titulo = titulo
        self.año = año
        
    # b) Método de clase
    @classmethod
    def obtener_total(cls):
        return cls.conteo_total

class Pelicula(Contenido):
    # c) Constructor con atributos propios y llamada a la clase padre
    def __init__(self, titulo, año, director, duracion):
        # Llama al __init__ de Contenido para sumar al contador e inicializar titulo y año
        super().__init__(titulo, año) 
        
        # Atributos exclusivos de una Película
        self.director = director
        self.duracion = duracion
        
    # d) Método de instancia para mostrar datos
    def mostrar_ficha(self):
        # Accedemos a los atributos heredados (titulo, año) y a los propios (director, duracion)
        print(f"Título: {self.titulo} ({self.año}) | Director: {self.director} |  {self.duracion} min")

# e) Pruebas instanciando con los nuevos parámetros
p1 = Pelicula("Interstellar", 2014, "Christopher Nolan", 169)
p2 = Pelicula("El Viaje de Chihiro", 2001, "Hayao Miyazaki", 125)
p3 = Pelicula("Matrix", 1999, "Lana y Lilly Wachowski", 136)

# Mostramos la ficha de una de las películas
p1.mostrar_ficha()

# Verificamos el contador global a través del método de clase
print(f"Total de películas en el catálogo: {Pelicula.obtener_total()}")