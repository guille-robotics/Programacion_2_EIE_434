// Ejemplo 7: Ejercicio Práctico - Punteros y NULL
#include <stdio.h>

int main() {
    int num1 = 10, num2 = 20;
    int *ptr1, *ptr2; 

    ptr1 = &num1;
    ptr2 = &num2;

    ptr1 = ptr2; // OJO: Igualamos punteros, no valores
    ptr2 = NULL; // NULL es "ninguna parte"
    
    printf("num1: %d, num2: %d\n", num1, num2);
    printf("*ptr1: %d\n", *ptr1);
    
    // printf("*ptr2: %d\n", *ptr2); // ¿Que pasaria aqui?

    return 0;
}