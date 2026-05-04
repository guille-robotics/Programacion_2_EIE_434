class Bateria:
    def __init__(self, marca):
        self.marca = marca
        self.__carga = 100  # Atributo privado

    def usar_bateria(self, gasto):
        self.__carga -= gasto
        if self.__carga <= 0:
            self.__carga = 0
            print("¡Batería agotada!")

    def ver_carga(self):
        return self.__carga

# --- Prueba del código ---
mi_bateria = Bateria("LiPo-Max")

print(f"Carga inicial: {mi_bateria.ver_carga()}%")

# Gastamos 40%
mi_bateria.usar_bateria(40)
print(f"Carga actual: {mi_bateria.ver_carga()}%")

# Gastamos 80% (debería agotarse y quedar en 0)
mi_bateria.usar_bateria(80)
print(f"Carga final: {mi_bateria.ver_carga()}%")