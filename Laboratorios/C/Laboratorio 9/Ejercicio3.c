#include <stdio.h>

int main() {
    int base, altura, area, perimetro;

    // Ingreso de datos
    printf("Ingrese la base del rectángulo: ");
    scanf("%d", &base);

    printf("Ingrese la altura del rectángulo: ");
    scanf("%d", &altura);

    // Cálculos
    area = base * altura;
    perimetro = (2 * base) + (2 * altura);

    // Salida de resultados
    printf("\n--- Resultados ---\n");
    printf("El área del rectángulo es: %d\n", area);
    printf("El perímetro del rectángulo es: %d\n", perimetro);

    return 0;
}