from abc import ABC, abstractmethod

# ==========================================
# 1. DEFINICIÓN DE CLASES (EL PLANO ABSTRACTO Y EL CÓMO)
# ==========================================

# Clase Padre Abstracta: Ya no es solo una sugerencia, ahora es un CONTRATO ESTRICTO.
# Al heredar de ABC, le decimos a Python que esta clase no se puede instanciar directamente.
class Unidad(ABC):
    
    # El decorador @abstractmethod obliga a que cualquier clase hija 
    # TENGA que programar su propia versión de este método.
    @abstractmethod
    def atacar(self):
        pass 

# Clases Hijas (Concretas): Cumplen con el contrato al pie de la letra.
class Arquero(Unidad):
    def atacar(self):
        print("El Arquero dispara una flecha perforante. (-10 HP)")

class Espadachin(Unidad):
    def atacar(self):
        print("El Espadachín da un corte transversal. (-15 HP)")

class Catapulta(Unidad):
    def atacar(self):
        print("La Catapulta lanza una roca gigante. (-50 HP)")


# ==========================================
# 2. MOTOR DEL JUEGO BASE (EL QUÉ)
# ==========================================

print("--- JUEGO BASE: PRIMERA BATALLA ---")

# Creamos nuestro ejército. Python nos deja porque Arquero, Espadachín 
# y Catapulta cumplieron con el contrato de tener un método atacar().
ejercito = [Arquero(), Espadachin(), Catapulta(), Arquero()]

for unidad in ejercito:
    unidad.atacar()


# ==========================================
# 3. LLEGA EL DLC: AGREGANDO EL DRAGÓN
# ==========================================

print("\n---  INSTALANDO EXPANSIÓN: EL DRAGÓN ---")

class Dragon(Unidad):
    def atacar(self):
        print("El Dragón escupe una llamarada devastadora. (-100 HP)")

ejercito.append(Dragon())
print("¡Dragón añadido con éxito!\n")

for unidad in ejercito:
    unidad.atacar()


# ==========================================
# 4. LA ABSTRACCIÓN EN ACCIÓN (EL ERROR FATAL)
# ==========================================

print("\n--- PRUEBA DE SEGURIDAD: EL CONTRATO ROTO ---")
print("Un programador novato intenta crear un Mago, pero olvida programar el ataque...")

# Creamos la clase, pero "olvidamos" poner el def atacar()
class MagoNovato(Unidad):
    def curar(self):
        print("✨ El Mago cura a un aliado.")

# --- PARA MOSTRAR EN CLASES: DESCOMENTA LA LÍNEA DE ABAJO ---
mago_1 = MagoNovato() 

# Si descomentas la línea anterior y ejecutas el código, Python lanzará este error:
# TypeError: Can't instantiate abstract class MagoNovato with abstract method atacar
# ¡La abstracción salvó el juego de un colapso en medio de la batalla!