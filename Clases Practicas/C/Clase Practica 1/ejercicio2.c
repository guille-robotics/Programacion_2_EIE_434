#include <stdio.h>

int main() {
    float x, resultado;
    
    printf("Ingrese el valor de x: ");
    scanf("%f", &x);
    
    if (x <= 0) {
        resultado = x + 3;
    } else {
        resultado = (x * x) + (2 * x);
    }
    
    printf("El valor de f(%.2f) es: %.2f\n", x, resultado);
    
    return 0;
}