// Ejemplo 9: Uso de scanf y printf con variables
#include <stdio.h>

int main() {
    int edad;
    
    printf("Ingrese su edad: ");
    
    // ¿Por que printf no usa '&' pero scanf si?
    scanf("%d", &edad); 
    
    return 0;
}