// ==========================================
// PROBLEMA 2: Interfaz HMI (Bucle Principal)
// ==========================================

int main() {
    // Instanciación de las estructuras
    Estanque tanque1;
    Estanque tanque2;
    
    // Inicialización pasando la dirección de memoria (&)
    Estanque_init(&tanque1, 1, 1000.0);
    Estanque_init(&tanque2, 2, 500.0);

    int opcion = 0;
    int seleccion_tanque;
    float cantidad;

    printf("=== SCADA / Panel HMI - Control de Estanques ===\n");

    // Bucle infinito de operación
    while (opcion != 3) {
        printf("\nMenu Principal:\n");
        printf("1. Inyectar fluido\n");
        printf("2. Monitorear niveles\n");
        printf("3. Apagar sistema\n");
        printf("Ingrese opcion: ");
        scanf("%d", &opcion);

        switch(opcion) {
            case 1:
                printf("Seleccione la ruta del fluido (Estanque 1 o 2): ");
                scanf("%d", &seleccion_tanque);
                printf("Ingrese cantidad de litros a inyectar: ");
                scanf("%f", &cantidad);

                // Lógica de Enrutamiento
                if (seleccion_tanque == 1) {
                    Estanque_llenar(&tanque1, cantidad);
                } else if (seleccion_tanque == 2) {
                    Estanque_llenar(&tanque2, cantidad);
                } else {
                    printf("\n[ERROR] ID de estanque no reconocido en la red.\n");
                }
                break;
                
            case 2:
                printf("\n--- Telemetria (Estado de Variables) ---\n");
                printf("Estanque 1: %.2f / %.2f L\n", tanque1.nivel_actual, tanque1.capacidad_maxima);
                printf("Estanque 2: %.2f / %.2f L\n", tanque2.nivel_actual, tanque2.capacidad_maxima);
                break;
                
            case 3:
                printf("\nDesconectando terminal HMI. Fin del ciclo.\n");
                break;
                
            default:
                printf("\n[ERROR] Comando invalido.\n");
        }
    }

    return 0;
}