print("Iniciando monitoreo del Datacenter...")

while True:
    temperatura = float(input("\nIngresa la lectura de temperatura (°C): "))
    
    # Evaluar los rangos de temperatura
    if 20 <= temperatura <= 45:
        print("Estado normal")
        
    elif 45 < temperatura <= 75:
        print("Advertencia: Encendiendo ventiladores auxiliares")
        
    elif temperatura > 75:
        print("¡Peligro Crítico! Apagando servidor de emergencia")
        break # Se sale del ciclo por emergencia