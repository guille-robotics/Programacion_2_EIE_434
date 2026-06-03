#include <stdio.h>

struct Luchador {
    int numero_entrada;
    
    /* * LA MAGIA DEL PUNTERO:
     * Al usar 'const char *' en lugar de 'char nombre[30]', no estamos
     * reservando 30 casilleros para letras. Solo estamos creando un pequeño
     * espacio (un puntero) que guardará la DIRECCIÓN de dónde está el texto.
     */
    const char *nombre; 
};

int main() {
    struct Luchador participante;
    
    participante.numero_entrada = 30;
    
    /* * El texto "Luchador Sorpresa A" vive en un lugar de solo lectura en la memoria.
     * Con el operador '=', simplemente le decimos al puntero: 
     * "Apunta a la dirección donde empieza esa frase".
     */
    participante.nombre = "Luchador Sorpresa A";
    
    printf("Entrada %d: %s\n", participante.numero_entrada, participante.nombre);
    
    /* * ¡REASIGNACIÓN DIRECTA!
     * Si esto fuera un char[], intentar usar '=' daría un error del compilador
     * porque no puedes mover un arreglo fijo. Pero como es un puntero, 
     * simplemente cambiamos la dirección a la que apunta.
     */
    participante.nombre = "Cody Rhodes";
    
    printf("¡Cambio de planes! Entrada %d: %s\n", participante.numero_entrada, participante.nombre);
    
    return 0;
}