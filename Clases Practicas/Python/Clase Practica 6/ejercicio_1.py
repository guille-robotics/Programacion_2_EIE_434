class Instrumento:
    # a) Atributo de clase
    unidad_estandar = 'SI'
    
    # Constructor de la clase padre con atributos compartidos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    # b) Método estático
    @staticmethod
    def convertir_a_base(valor_mili):
        return valor_mili / 1000

class Osciloscopio(Instrumento):
    # c) Constructor del hijo utilizando super()
    def __init__(self, marca, modelo):
        # Llamamos al constructor del padre para inicializar marca y modelo
        super().__init__(marca, modelo) 
        # Atributo exclusivo del hijo
        self.v_div = 1.0 
        
    # d) Método para actualizar y método para imprimir configuración
    def actualizar_v_div(self, nuevo_valor):
        self.v_div = nuevo_valor
        
    def imprimir_configuracion(self):
        # Accedemos a los atributos heredados, al propio y al de clase
        print(f"[{self.marca} {self.modelo}] Voltaje/Div: {self.v_div} | Sistema: {self.unidad_estandar}")

# e) Pruebas de instanciación
# Al instanciar, pasamos los argumentos requeridos por el constructor
mi_osciloscopio = Osciloscopio(marca="Rigol", modelo="DS1054Z")

mi_osciloscopio.actualizar_v_div(0.5)
mi_osciloscopio.imprimir_configuracion()

# Uso del método estático desde la clase
valor_mV = 500
valor_V = Instrumento.convertir_a_base(valor_mV)
print(f"{valor_mV} mV equivalen a {valor_V} V en la unidad base.")