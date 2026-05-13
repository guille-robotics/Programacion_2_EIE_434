#include <stdio.h>

int main() {
    int num1, num2;
    
    printf("Ingresa el primer número entero: ");
    scanf("%d", &num1);
    printf("Ingresa el segundo número entero: ");
    scanf("%d", &num2);

    // Operaciones aritméticas 
    printf("Suma: %d\n", num1 + num2);
    printf("Resta: %d\n", num1 - num2);
    printf("Multiplicación: %d\n", num1 * num2);
    printf("División (entera): %d\n", num1 / num2); // 
    printf("Módulo (resto): %d\n", num1 % num2); // 

    return 0;
}