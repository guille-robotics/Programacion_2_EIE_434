class Persona:
    # a) Clase base con atributos simples
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

class Estudiante(Persona):
    # b) Clase derivada con lista y carrera
    def __init__(self, nombre, rut, carrera):
        super().__init__(nombre, rut)
        self.carrera = carrera
        self.notas = [] # Se inicializa vacía
        
    # c) Métodos de instancia para notas y promedio
    def agregar_nota(self, nota):
        self.notas.append(nota)
        
    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)
        
    # d) Método para validar el acceso devolviendo un booleano
    def validar_acceso(self):
        promedio = self.calcular_promedio()
        if promedio >= 4.0:
            return True
        else:
            return False

# e) Pruebas de acceso al laboratorio
alumno_ia = Estudiante("J. Antias", "12.345.678-9", "Ingeniería Electrónica")

# Agregamos las notas requeridas
alumno_ia.agregar_nota(3.5)
alumno_ia.agregar_nota(4.2)
alumno_ia.agregar_nota(5.0)

promedio_final = alumno_ia.calcular_promedio()
print(f"El alumno {alumno_ia.nombre} tiene promedio {promedio_final:.1f}")

# Validamos el acceso
if alumno_ia.validar_acceso():
    print("ACCESO CONCEDIDO: Puede ingresar al Laboratorio de IA.")
else:
    print("ACCESO DENEGADO: Promedio insuficiente.")