#include <stdio.h>

// Función que evalúa la temperatura y retorna un código de estado
int evaluarTemperatura(float temp) {
    if (temp < 60.0) {
        return 0; // Normal
    } else if (temp >= 60.0 && temp <= 85.0) {
        return 1; // Advertencia
    } else {
        return 2; // Peligro
    }
}

int main() {
    float temperaturaActual;
    int estado;

    printf("--- Sistema de Monitoreo de Motor ---\n");

    // Ciclo para leer 5 temperaturas
    for (int i = 1; i <= 5; i++) {
        printf("\nIngrese la lectura de temperatura %d (Celsius): ", i);
        scanf("%f", &temperaturaActual);

        estado = evaluarTemperatura(temperaturaActual);

        // Uso de switch para evaluar la condición de retorno de la función
        switch (estado) {
            case 0:
                printf("Estado: NORMAL. El motor opera correctamente.\n");
                break;
            case 1:
                printf("Estado: ADVERTENCIA. Preste atencion a la refrigeracion.\n");
                break;
            case 2:
                printf("Estado: PELIGRO. Riesgo de dano termico inminente.\n");
                break;
            default:
                printf("Error en la lectura del estado.\n");
        }
    }

    return 0;
}