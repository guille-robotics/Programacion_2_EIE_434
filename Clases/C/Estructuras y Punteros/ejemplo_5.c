// Ejemplo 5: Punteros y variables normales
#include <stdio.h>

int main() {
    int x = 10;        // Variable normal
    int *p = &x;       // 'p' guarda la direccion de 'x'

    // Imprimiendo conceptos:
    printf("Valor de x: %d\n", x);
    printf("Direccion de x: %p\n", &x);
    printf("Valor del puntero p: %p\n", p);
    printf("Valor AL QUE APUNTA p: %d\n", *p);
    
    return 0;
}