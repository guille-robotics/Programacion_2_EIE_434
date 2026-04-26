class Termostato:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        # Atributo privado: el doble guion bajo evita modificaciones directas
        self.__temperatura = 20  

    # Getter: Permite leer el valor de forma segura
    def get_temperatura(self):
        return self.__temperatura

    # Setter: Actúa como filtro de seguridad antes de modificar el valor
    def set_temperatura(self, valor):
        if 15 <= valor <= 30:
            self.__temperatura = valor
            print(f"[{self.ubicacion}] Temperatura ajustada a {self.__temperatura}°C.")
        else:
            print(f"[{self.ubicacion}] Error: Temperatura de {valor}°C fuera de rango seguro (15-30°C).")

# --- Bloque de Pruebas ---
if __name__ == "__main__":
    print("--- Prueba Ejercicio 1 ---")
    termostato_sala = Termostato("Sala de Reuniones")
    
    # Lectura inicial
    print(f"Temperatura inicial: {termostato_sala.get_temperatura()}°C")
    
    # Intentos de modificación
    termostato_sala.set_temperatura(24)  # Modificación válida
    termostato_sala.set_temperatura(50)  # Modificación inválida (bloqueada)
    
    # Comprobación de que el valor peligroso no ingresó al sistema
    print(f"Temperatura actual: {termostato_sala.get_temperatura()}°C\n")