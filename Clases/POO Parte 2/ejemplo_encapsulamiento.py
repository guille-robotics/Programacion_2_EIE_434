class JugadorFutbol:
    def __init__(self, nombre):
        self.nombre = nombre       # Atributo Público
        self.__energia = 100       # Atributo Privado (Protegido por el doble guion bajo)

    # --- GETTER ---
    # Método para "leer" el valor de forma segura
    def get_energia(self):
        return self.__energia

    # --- SETTER ---
    # Método para "modificar" el valor pasando por una "aduana" de seguridad
    def set_energia(self, valor):
        # 1. Validar que sea un número entero
        if not isinstance(valor, int):
            print(f"Error: La energía debe ser un número. '{valor}' no es válido.")
        
        # 2. Validar que no sea negativa
        elif valor < 0:
            print("Aduana: No se puede tener energía negativa. Ajustando a 0.")
            self.__energia = 0
            
        # 3. Validar que no supere el límite
        elif valor > 100:
            print("Aduana: La energía máxima es 100. Ajustando a 100.")
            self.__energia = 100
            
        # 4. Si pasa todas las pruebas, actualizamos el estado
        else:
            self.__energia = valor

    # --- MÉTODOS DE ACCIÓN ---
    # Estos interactúan con el entorno usando la energía controlada
    def correr(self):
        if self.__energia >= 10:
            self.__energia -= 10
            print(f"[{self.nombre}] corre a toda velocidad. Energía restante: {self.__energia}")
        else:
            print(f"[{self.nombre}] está demasiado cansado para correr.")


# ==========================================
# SIMULACIÓN (Para ejecutar en clases)
# ==========================================

print("--- 1. CREANDO AL JUGADOR ---")
jugador1 = JugadorFutbol("Alexis")
print(f"Jugador creado: {jugador1.nombre}")
print(f"Energía inicial: {jugador1.get_energia()}")

print("\n--- 2. INTENTANDO HACER TRAMPA (Hackeando lo público) ---")
# Si el alumno intenta acceder directo, Python crea una variable nueva, 
# no modifica la privada real.
jugador1.__energia = 5000 
print("¡Se intentó subir la energía a 5000 directamente!")
print(f"Energía real del sistema: {jugador1.get_energia()} (¡La trampa falló!)")

print("\n--- 3. PONIENDO A PRUEBA LA ADUANA (Setter) ---")
# Error de tipo
jugador1.set_energia("Cansado")

# Error matemático (número negativo)
jugador1.set_energia(-50)
print(f"Energía después del error negativo: {jugador1.get_energia()}")

print("\n--- 4. JUGANDO NORMALMENTE ---")
# Le damos un valor válido (20) y lo hacemos correr hasta que se canse
jugador1.set_energia(20)

jugador1.correr() # Gasta 10, queda 10
jugador1.correr() # Gasta 10, queda 0
jugador1.correr() # Intenta correr, pero el objeto sabe que ya no tiene energía