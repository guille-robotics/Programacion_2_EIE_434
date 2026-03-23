def calibrar_robot(*args, **kwargs):
    print("=== Iniciando secuencia de calibración ===")
    
    # Procesamiento de *args (Ángulos)
    articulaciones_moviendose = len(args)
    desplazamiento_total = sum(args)
    
    print(f"Articulaciones en movimiento: {articulaciones_moviendose}")
    print(f"Desplazamiento angular total calculado: {desplazamiento_total}°")
    
    print("\n--- Parámetros de Configuración ---")
    # Procesamiento de **kwargs (Configuraciones)
    for clave, valor in kwargs.items():
        # Verificación específica de seguridad
        if clave == "torque_max" and valor > 100:
            print(f"⚠️ ADVERTENCIA: Peligro de sobrecarga (Torque al {valor}%)")
        else:
            print(f"{clave.capitalize()} : {valor}")
            
    print("=========================================\n")

# Ejecución de prueba con 4 ángulos y 3 parámetros de configuración
calibrar_robot(45, 90, -30, 15, velocidad=50, torque_max=120, herramienta="pinza")