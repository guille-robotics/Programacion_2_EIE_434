class PistaAudio:
    # a) Atributo de clase
    plataforma = 'Spotify'
    
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion # en segundos
        
    # b) Método estático
    @staticmethod
    def formatear_tiempo(segundos):
        minutos = segundos // 60
        seg_restantes = segundos % 60
        return f"{minutos}:{seg_restantes:02d}"

class Cancion(PistaAudio):
    # c) Clase hija y nuevos atributos
    def __init__(self, titulo, duracion, artista, genero):
        super().__init__(titulo, duracion)
        self.artista = artista
        self.genero = genero
        
    # d) Método de instancia dinámico
    def reproducir(self):
        print("¡Subiendo el volumen! ")
        print(f"Escuchando '{self.titulo}' de {self.artista} ({self.genero}) en {self.plataforma}... ")

# e) Pruebas con la canción favorita
mi_cancion = Cancion("Creep", 238, "Radiohead", "Rock Alternativo")

# Usamos el método estático para formatear los 238 segundos
tiempo_str = PistaAudio.formatear_tiempo(mi_cancion.duracion)
print(f"Duración de la canción: {tiempo_str}")

# Ejecutamos la reproducción
mi_cancion.reproducir()