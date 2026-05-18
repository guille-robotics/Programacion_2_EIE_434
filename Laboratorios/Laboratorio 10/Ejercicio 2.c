#include <stdio.h>

int main() {
    int opcion;

    do {
        printf("\n=== Panel de Control ===\n");
        printf("1. Activar Motor\n");
        printf("2. Detener Motor\n");
        printf("3. Leer Estado\n");
        printf("4. Salir\n");
        printf("Ingrese su opcion: ");
        scanf("%d", &opcion);

        switch(opcion) {
            case 1:
                printf("\n[OK] Acción: Motor activado.\n");
                break;
            case 2:
                printf("\n[OK] Acción: Motor detenido.\n");
                break;
            case 3:
                printf("\n[OK] Acción: Leyendo estado de los sensores...\n");
                break;
            case 4:
                printf("\nSaliendo del panel de control...\n");
                break;
            default:
                printf("\n[ERROR] Opción no válida. Intente nuevamente.\n");
                break;
        }
    } while(opcion != 4);

    return 0;
}