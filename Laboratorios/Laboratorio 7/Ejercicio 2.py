# 1. Clase padre
class Sensor:
    def medir(self):
        print("Midiendo datos base...")

# 2. Clase hija 1 (Sensor de Temperatura)
class SensorTemperatura(Sensor):
    def medir(self):
        print("Midiendo temperatura en grados Celsius")

# 3. Clase hija 2 (Sensor de Luz)
class SensorLuz(Sensor):
    def medir(self):
        print("Midiendo nivel de luz en Lux")

# 4. Función independiente para demostrar el polimorfismo
def iniciar_medicion(sensor_cualquiera):
    # La magia del polimorfismo: la función no sabe (ni le importa) 
    # qué tipo de sensor recibe, solo sabe que debe ejecutar medir()
    sensor_cualquiera.medir()

# --- Pruebas del código ---

# Instanciamos los objetos
mi_sensor_temp = SensorTemperatura()
mi_sensor_luz = SensorLuz()
sensor_generico = Sensor()

# Llamamos a la misma función pasándole objetos diferentes
print("--- Prueba 1 ---")
iniciar_medicion(mi_sensor_temp)

print("\n--- Prueba 2 ---")
iniciar_medicion(mi_sensor_luz)

print("\n--- Prueba 3 (Sensor Base) ---")
iniciar_medicion(sensor_generico)