#include <stdio.h>

int main() {
    int n, i;
    long long t1 = 0, t2 = 1, siguiente_termino;

    printf("Ingrese la cantidad de terminos para la serie de Fibonacci: ");
    scanf("%d", &n);

    printf("Serie de Fibonacci: ");

    for (i = 1; i <= n; ++i) {
        printf("%lld, ", t1);
        siguiente_termino = t1 + t2;
        t1 = t2;
        t2 = siguiente_termino;
    }
    
    printf("\n");
    return 0;
}