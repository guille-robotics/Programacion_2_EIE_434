#include <stdio.h>

int main() {
    int fecha;
    int ano_actual = 2026; // Asumimos el año actual
    
    printf("Hola\n");
    printf("Por favor introduzca el año en que nacio: ");
    scanf("%d", &fecha);
    
    int edad = ano_actual - fecha;
    
    printf("Si usted nacio en %d este ano cumple %d anos.\n", fecha, edad);
    
    return 0;
}