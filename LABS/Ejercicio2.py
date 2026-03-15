# Solicitar datos iniciales
voltaje = float(input("Ingresa el voltaje inicial del banco de baterías: "))
voltaje_minimo = float(input("Ingresa el voltaje mínimo de operación: "))
horas = 0

# Ciclo de descarga
while voltaje > voltaje_minimo:
    voltaje *= 0.97  # El voltaje decae un 3% por hora
    horas += 1       # Se suma una hora de uso

# Resultados finales
print(f"\nEl banco de baterías logró entregar energía durante {horas} horas enteras.")
print(f"Voltaje final estimado al detenerse: {voltaje:.2f} V")