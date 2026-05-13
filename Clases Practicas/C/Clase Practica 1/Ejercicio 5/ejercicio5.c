#include <stdio.h>
#include <time.h>

int main() {
    // 1. Registrar el tiempo de inicio
    clock_t start_time = clock();

    // --- CÓDIGO A MEDIR ---
    // Ejemplo: Un bucle que suma mil millones de números
    long long suma = 0;
    for(long long i = 0; i < 1000000000; i++) {
        suma += i;
    }
    // ----------------------

    // 2. Registrar el tiempo de fin
    clock_t end_time = clock();

    // 3. Calcular el tiempo transcurrido en segundos
    // Se divide por CLOCKS_PER_SEC para convertir los "ticks" a segundos
    double time_spent = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("Resultado de la suma: %lld\n", suma);
    printf("Tiempo de ejecución en C: %f segundos\n", time_spent);

    return 0;
}