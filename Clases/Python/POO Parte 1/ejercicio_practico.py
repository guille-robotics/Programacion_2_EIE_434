# ==========================================
# PROYECTO PLAYABOT: Control de Flota
# Conceptos: POO, Herencia, Tipos de Métodos
# ==========================================

class UnidadAutonoma:
    """Superclase que define el comportamiento base de cualquier unidad de la flota."""
    
    # Atributo de Clase
    total_unidades = 0 

    def __init__(self, id_unidad):
        self.id = id_unidad
        self.bateria = 100
        # Cada vez que se crea cualquier tipo de unidad, sumamos 1 al total
        UnidadAutonoma.total_unidades += 1

    # 1. Método de Instancia (Heredable)
    def ir_a_base(self):
        self.bateria = 100
        print(f"[{self.id}] En base. Batería recargada al 100%.")

    # 2. Método de Clase
    @classmethod
    def reporte_flota(cls):
        print(f"\n--- REPORTE: Flota activa con {cls.total_unidades} unidades ---")

    # 3. Método Estático
    @staticmethod
    def clima_seguro(viento_kmh):
        # Operación segura solo si el viento es menor a 40 km/h
        return viento_kmh < 40


class RobotLimpiador(UnidadAutonoma):
    """Subclase terrestre especializada en recolectar basura."""
    
    def __init__(self, id_robot):
        # Llamamos al constructor del Padre para inicializar ID y Batería
        super().__init__(id_robot) 
        self.basura_recolectada = 0
        
    def recolectar(self, kilos):
        consumo = kilos * 2
        if self.bateria >= consumo:
            self.basura_recolectada += kilos
            self.bateria -= consumo
            print(f"[{self.id}] Terrestre: Recolectó {kilos}kg. Batería rest: {self.bateria}%")
        else:
            print(f"[{self.id}] Terrestre: Batería insuficiente para recolectar {kilos}kg.")


class DronAereo(UnidadAutonoma):
    """Subclase aérea especializada en exploración."""
    
    def __init__(self, id_unidad, resolucion_camara):
        # Llamamos al constructor del Padre
        super().__init__(id_unidad) 
        self.camara = resolucion_camara
        
    def mapear_zona(self): 
        if self.bateria >= 15:
            self.bateria -= 15
            print(f"[{self.id}] Aéreo: Mapeando playa en {self.camara}. Batería rest: {self.bateria}%")
        else:
            print(f"[{self.id}] Aéreo: Batería baja para volar.")


# ==========================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    
    print("Iniciando Sistema Playabot...\n")
    
    # 1. Validación usando el Método Estático (Sin instanciar nada)
    viento_actual = 35
    print(f"Condición de viento: {viento_actual} km/h")
    
    if not UnidadAutonoma.clima_seguro(viento_actual):
        print("ALERTA AMBIENTAL: Operación cancelada por clima peligroso.")
    else:
        print("Clima óptimo. Desplegando unidades...\n")
        
        # 2. Instanciación (Polimorfismo: creamos distintos tipos)
        playabot_1 = RobotLimpiador("PLY-01")
        halcon_1 = DronAereo("DRN-01", resolucion_camara="4K")
        
        # 3. Uso del Método de Clase
        UnidadAutonoma.reporte_flota()
        print("-" * 40)
        
        # 4. Métodos propios de cada subclase
        halcon_1.mapear_zona()
        playabot_1.recolectar(15)
        playabot_1.recolectar(40) # Intentamos gastar mucha batería
        
        print("\nRetornando flota...")
        
        # 5. Métodos heredados (Ambos usan la misma función del Padre)
        halcon_1.ir_a_base()
        playabot_1.ir_a_base()