# ==========================================
# 1. DEFINICIÓN DE CLASES (EL CÓMO)
# ==========================================

# Clase Padre: Establece la regla de que todas las unidades deben poder atacar.
class Unidad:
    def atacar(self):
        pass # Se deja vacío. Las clases hijas se encargarán de rellenarlo.

# Clases Hijas: Cada una sobreescribe el método a su manera.
class Arquero(Unidad):
    def atacar(self):
        print(" El Arquero dispara una flecha perforante. (-10 HP)")

class Espadachin(Unidad):
    def atacar(self):
        print("El Espadachín da un corte transversal. (-15 HP)")

class Catapulta(Unidad):
    def atacar(self):
        print("La Catapulta lanza una roca gigante. (-50 HP)")

# ==========================================
# 2. MOTOR DEL JUEGO BASE (EL QUÉ)
# ==========================================

print("--- 🎮 JUEGO BASE: PRIMERA BATALLA ---")

# Creamos nuestro ejército mezclado
ejercito = [Arquero(), Espadachin(), Catapulta(), Arquero()]

# ¡LA MAGIA DEL POLIMORFISMO!
# El motor del juego no usa ningún "if". No le importa qué unidad es cuál.
# Solo confía en que todas saben "atacar()".
for unidad in ejercito:
    unidad.atacar()


# ==========================================
# 3. LLEGA EL DLC: AGREGANDO EL DRAGÓN
# ==========================================

print("\n--- INSTALANDO EXPANSIÓN: EL DRAGÓN ---")

# Para agregar una unidad nueva, NO tocamos el motor del juego. 
# Solo creamos un módulo nuevo e independiente.
class Dragon(Unidad):
    def atacar(self):
        print("El Dragón escupe una llamarada devastadora. (-100 HP)")

# Agregamos al Dragón a nuestra lista de tropas
ejercito.append(Dragon())

print("¡Dragón añadido con éxito sin romper el código original!\n")

# ==========================================
# 4. MOTOR DEL JUEGO (ACTUALIZADO)
# ==========================================

print("--- JUEGO ACTUALIZADO: SEGUNDA BATALLA ---")

# Fíjate que este es EXACTAMENTE el mismo bucle 'for' de arriba.
# No le agregamos ningún "elif type(unidad) == Dragon".
# El motor sigue funcionando y ahora procesa al Dragón automáticamente.
for unidad in ejercito:
    unidad.atacar()