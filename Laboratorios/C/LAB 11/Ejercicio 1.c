#include <stdio.h>

int main() {
    int N;
    int contador = 0;

    printf("Ingrese el valor limite N: ");
    scanf("%d", &N);

    printf("Tren de pulsos (valores pares): ");
    
    // Bucle for que itera desde 0 hasta N
    for (int i = 0; i <= N; i++) {
        // Se usa el operador módulo para identificar pares
        if (i % 2 == 0) {
            printf("%d ", i);
            contador++; // Incrementa el contador de pares encontrados
        }
    }

    printf("\nTotal de numeros pares detectados: %d\n", contador);

    return 0;
}