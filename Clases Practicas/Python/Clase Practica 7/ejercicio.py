from abc import ABC, abstractmethod

# ==========================================
# SOLUCIONARIO: PROYECTO INTEGRADOR DE ROBÓTICA
# ==========================================

# --- FASE 1 y FASE 4: Clase Base y Abstracción ---
class RobotMovil(ABC):
    estado_red = 'Desconectado' # Atributo de clase

    def __init__(self, nombre, tipo_sensor):
        self.nombre = nombre
        self.tipo_sensor = tipo_sensor
        
    def conectar_red(self):
        RobotMovil.estado_red = 'Conectado'
        print(f"[{self.nombre}] se ha conectado a la red central.")

    def reportar_estado(self):
        print(f"Robot: {self.nombre} | Sensor: {self.tipo_sensor} | Red: {RobotMovil.estado_red}")

    # Método abstracto (Añadido en la Fase 4)
    @abstractmethod
    def procesar_entorno(self):
        pass


# --- FASE 2 y FASE 3: Herencia y Encapsulamiento ---
class RobotLimpieza(RobotMovil):
    def __init__(self, nombre, tipo_sensor):
        super().__init__(nombre, tipo_sensor)
        self.__capacidad_carga = 0 # (Fase 3) Atributo privado

    # --- GETTER Y SETTER (Fase 3) ---
    def get_carga(self):
        return self.__capacidad_carga

    def set_carga(self, nueva_carga):
        if nueva_carga < 0:
            print("Error: La carga no puede ser negativa.")
        elif nueva_carga > 100:
            print("Error: Excede el límite de carga (Max 100).")
        else:
            self.__capacidad_carga = nueva_carga

    # --- MÉTODOS DE INSTANCIA ---
    def recolectar_basura(self, cantidad):
        # Utilizando el getter y setter para la lógica interna (Fase 3)
        carga_actual = self.get_carga()
        self.set_carga(carga_actual + cantidad)
        print(f"[{self.nombre}] Carga actual: {self.get_carga()}/100")

    # Cumpliendo el contrato de abstracción (Fase 4)
    def procesar_entorno(self):
        print(f"[{self.nombre}] Escaneando suelo y aspirando residuos.")


# --- FASE 4: Nueva clase hija ---
class RobotVigilancia(RobotMovil):
    def __init__(self, nombre, tipo_sensor):
        super().__init__(nombre, tipo_sensor)
        self.camara_activa = True

    # Cumpliendo el contrato de abstracción
    def procesar_entorno(self):
        print(f"[{self.nombre}] Analizando video en busca de intrusos.")


# ==========================================
# PRUEBAS DE EJECUCIÓN 
# ==========================================

print("--- PRUEBA FASE 1 ---")
# Instanciamos la hija porque la padre ahora es abstracta
robot1 = RobotLimpieza("Alpha", "LIDAR") 
robot1.conectar_red()
robot1.reportar_estado()

print("\n--- PRUEBA FASE 2 y 3 ---")
robot_limpieza = RobotLimpieza("Wall-E", "Infrarrojo")
robot_limpieza.recolectar_basura(5)
robot_limpieza.recolectar_basura(150) # Prueba de error del setter

print("\n--- PRUEBA FASE 4 ---")
flota = [
    RobotLimpieza("Limpiador-X", "LIDAR"),
    RobotVigilancia("Centinela-1", "Cámara Térmica")
]

# Polimorfismo en acción
for robot in flota:
    robot.procesar_entorno()