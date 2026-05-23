// Ejemplo 6: Modificando el valor a través de un puntero
#include <stdio.h>

int main() {
    int x = 20;
    int *p = &x;  // 'p' apunta a 'x'
    
    printf("Valor original de x: %d\n", x); // Imprime 20

    // ¡Viajamos a la direccion y cambiamos el valor!
    *p = 30; 
    
    printf("Nuevo valor de x: %d\n", x);    // Imprime 30

    return 0;
}