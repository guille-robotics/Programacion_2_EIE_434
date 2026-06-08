#include <stdio.h>

// 1. Función que recibe un puntero
void duplicarValor(int *numero) {
    // 2. Modificamos directamente el valor en la memoria
    *numero = *numero * 2;
}

int main() {
    // 3. Declaración de la variable
    int voltaje = 12;
    
    printf("Valor ANTES de la funcion: %d V\n", voltaje);

    // 4. Llamada a la función enviando la DIRECCIÓN de memoria (&)
    duplicarValor(&voltaje);

    // 5. Comprobación del cambio
    printf("Valor DESPUES de la funcion: %d V\n", voltaje);

    return 0;
}