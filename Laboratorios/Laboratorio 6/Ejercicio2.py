class Instrumento:
    def __init__(self, marca):
        self.marca = marca
        self.estado = "Apagado"
        
    def encender(self):
        self.estado = "Encendido"
        print(f"[{self.marca}] El equipo ha sido encendido.")
        
    # Método estático: Herramienta de utilidad que no necesita 'self'
    @staticmethod
    def validar_voltaje(voltaje):
        return voltaje <= 220

class Osciloscopio(Instrumento):
    def __init__(self, marca, canales):
        # super() llama al constructor de la clase padre (Instrumento)
        super().__init__(marca) 
        self.canales = canales
        
    # Método exclusivo del osciloscopio
    def medir_senal(self):
        if self.estado == "Encendido":
            print(f"[{self.marca}] Midiendo señal en los {self.canales} canales.")
        else:
            print(f"[{self.marca}] Error: No se puede medir, el osciloscopio está apagado.")

# --- Bloque de Pruebas ---
if __name__ == "__main__":
    print("--- Prueba Ejercicio 2 ---")
    
    # Uso del método estático sin instanciar ningún objeto
    voltaje_red = 300
    es_seguro = Instrumento.validar_voltaje(voltaje_red)
    print(f"¿Es seguro conectar a {voltaje_red}V?: {es_seguro}")
    
    # Uso de la clase hija
    mi_osciloscopio = Osciloscopio("Tektronix", 4)
    mi_osciloscopio.medir_senal()  # Fallará porque está apagado
    mi_osciloscopio.encender()     # Método heredado del padre
    mi_osciloscopio.medir_senal()  # Ahora sí funcionará
    print()