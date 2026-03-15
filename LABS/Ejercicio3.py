while True:
    # Desplegar el menú
    print("\n--- Menú de Conversión ---")
    print("1. Convertir miliamperios (mA) a amperios (A)")
    print("2. Convertir microfaradios (uF) a faradios (F)")
    print("3. Convertir kiloohmios (kOhm) a ohmios (Ohm)")
    print("4. Salir")
    
    opcion = int(input("Elige una opción (1-4): "))
    
    # Evaluar las opciones con if/elif/else
    if opcion == 1:
        ma = float(input("Ingresa el valor en mA: "))
        print(f"> {ma} mA equivalen a {ma / 1000} A")
        
    elif opcion == 2:
        uf = float(input("Ingresa el valor en uF: "))
        print(f"> {uf} uF equivalen a {uf / 1000000} F")
        
    elif opcion == 3:
        kohm = float(input("Ingresa el valor en kOhm: "))
        print(f"> {kohm} kOhm equivalen a {kohm * 1000} Ohmios")
        
    elif opcion == 4:
        print("Saliendo del programa...")
        break # Termina el ciclo y sale del menú
        
    else:
        print("Opción no válida. Por favor, ingresa un número entre 1 y 4.")