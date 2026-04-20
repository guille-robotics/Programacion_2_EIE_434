from abc import ABC, abstractmethod

# Clase Abstracta: Sirve como plano/contrato, no se puede instanciar directamente
class Motor(ABC):
    def __init__(self, id_motor):
        self.id_motor = id_motor
        
    # Método abstracto: Obliga a las clases hijas a crearlo sí o sí
    @abstractmethod
    def accionar(self):
        pass

# Clase Concreta 1
class MotorPasoAPaso(Motor):
    def accionar(self):
        print(f"[{self.id_motor}] Motor Paso a Paso: Girando en pasos de 1.8 grados.")

# Clase Concreta 2
class Servomotor(Motor):
    def accionar(self):
        print(f"[{self.id_motor}] Servomotor: Posicionando el eje a 90 grados.")

# --- Bloque de Pruebas ---
if __name__ == "__main__":
    print("--- Prueba Ejercicio 3 ---")
    
    # Instanciamos los actuadores específicos
    motor_1 = MotorPasoAPaso("NEMA-17")
    motor_2 = Servomotor("SG90")
    
    # Los agrupamos en una lista (simulando una línea de ensamblaje)
    linea_produccion = [motor_1, motor_2]
    
    print("Iniciando secuencia de control:")
    # POLIMORFISMO EN ACCIÓN: 
    # El bucle envía la misma orden a todos, y cada objeto responde a su manera.
    for actuador in linea_produccion:
        actuador.accionar()