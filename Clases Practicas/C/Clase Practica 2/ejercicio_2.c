#include <stdio.h>

// Función que calcula la resistencia equivalente
float calcularResistencia() {
    int tipo, n;
    float resistencia, req = 0.0;

    printf("Seleccione la configuracion:\n");
    printf("1. Serie\n");
    printf("2. Paralelo\n");
    printf("Opcion: ");
    scanf("%d", &tipo);

    printf("Ingrese la cantidad de resistores (N): ");
    scanf("%d", &n);

    // Ciclo para procesar N resistores
    for (int i = 1; i <= n; i++) {
        printf("Ingrese el valor del resistor %d (Ohms): ", i);
        scanf("%f", &resistencia);

        // Condicional para descartar valores erróneos
        if (resistencia <= 0) {
            printf("Error: Valor invalido. No se considerara en el calculo.\n");
            i--; // Para repetir la iteración actual
            continue;
        }

        // Condicional según el tipo de circuito
        if (tipo == 1) {
            req += resistencia; // Serie: suma directa
        } else if (tipo == 2) {
            req += (1.0 / resistencia); // Paralelo: suma de inversos
        }
    }

    // Si es paralelo, se debe invertir el resultado final (y evitar división por cero)
    if (tipo == 2 && req > 0) {
        req = 1.0 / req;
    }

    return req;
}

int main() {
    printf("--- Calculadora de Resistencias Equivalentes ---\n");
    float resultado = calcularResistencia();
    
    if(resultado > 0) {
        printf("\nLa resistencia equivalente es: %.2f Ohms\n", resultado);
    }else {
        printf("\nNo se pudo calcular la resistencia equivalente debido a valores invalidos.\n");
    }
    
    return 0;
}