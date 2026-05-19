#include <stdio.h>

int main() {
    int temperatura;

    printf("Ingrese el valor de la temperatura en °C: ");
    scanf("%d", &temperatura);

    if (temperatura < 20) {
        printf("Estado: Subenfriamiento\n");
    } else if (temperatura >= 20 && temperatura <= 45) {
        printf("Estado: Operación Nominal\n");
    } else {
        printf("Estado: Alarma de Sobrecalentamiento\n");
    }

    return 0;
}