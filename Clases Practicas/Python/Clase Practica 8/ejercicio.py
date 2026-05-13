import numpy as np
import matplotlib.pyplot as plt

class Personaje:
    def __init__(self, nombre, hp_maximo, ataque_base):
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.ataque_base = ataque_base
        
        # ENCAPSULAMIENTO ESTRICTO: Atributo privado con doble guion bajo
        # Python oculta esta variable. Si alguien intenta hacer heroe.__hp_actual = 1000, 
        # el programa arrojará un error.
        self.__hp_actual = hp_maximo
        
        self.historial_hp = [hp_maximo]

    def esta_vivo(self):
        return self.__hp_actual > 0

    # Interfaz pública controlada para alterar la variable privada
    def recibir_dano(self, cantidad):
        self.__hp_actual -= cantidad
        
        # VALIDACION: La vida no puede ser negativa
        if self.__hp_actual < 0:
            self.__hp_actual = 0
            
        self.historial_hp.append(self.__hp_actual)

    def atacar(self, objetivo, turno):
        if turno % 3 == 0:
            dano_final = self.ataque_base * 2
            print(f"¡GOLPE CRÍTICO! {self.nombre} ataca a {objetivo.nombre} con {dano_final} de daño.")
        else:
            dano_final = self.ataque_base
            print(f"{self.nombre} ataca a {objetivo.nombre} con {dano_final} de daño.")
            
        # El daño se aplica mediante el método público, respetando el encapsulamiento
        objetivo.recibir_dano(dano_final)

# ==========================================
# Ejecución del programa
# ==========================================
if __name__ == "__main__":
    
    heroe = Personaje(nombre="Sir Electrón", hp_maximo=100, ataque_base=15)
    dragon = Personaje(nombre="Dragón de Código Espagueti", hp_maximo=150, ataque_base=12)

    turno_actual = 1
    print("¡INICIA EL COMBATE!\n")

    while heroe.esta_vivo() and dragon.esta_vivo():
        print(f"--- TURNO {turno_actual} ---")
        
        heroe.atacar(dragon, turno_actual)
        
        if dragon.esta_vivo():
            dragon.atacar(heroe, turno_actual)
            
        turno_actual += 1
        print("")

    print("--- COMBATE TERMINADO ---")
    if heroe.esta_vivo():
        print(f"¡{heroe.nombre} ha salido victorioso!")
    else:
        print(f"¡{heroe.nombre} ha caído en batalla...")

    # Procesamiento y Gráficos
    hp_heroe_array = np.array(heroe.historial_hp)
    hp_dragon_array = np.array(dragon.historial_hp)
    eje_x_turnos = np.arange(len(hp_heroe_array))

    plt.figure(figsize=(10, 5))
    plt.plot(eje_x_turnos, hp_heroe_array, label=heroe.nombre, color='blue', marker='o', linewidth=2)
    plt.plot(eje_x_turnos, hp_dragon_array, label=dragon.nombre, color='red', marker='x', linewidth=2)

    plt.title("Desarrollo del Combate: Historial de HP")
    plt.xlabel("Turno")
    plt.ylabel("Puntos de Vida (HP)")
    plt.axhline(0, color='black', linestyle='--')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()