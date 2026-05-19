#include <stdio.h>

// Función que simula el recorrido del robot
int realizarMision(int distanciaObjetivo, int bateria) {
    int tipoTerreno;

    // El ciclo evalúa dos condiciones lógicas directamente
    while (distanciaObjetivo > 0 && bateria > 0) {
        printf("\nDistancia restante: %d m | Bateria: %d%%\n", distanciaObjetivo, bateria);
        printf("Ingrese tipo de terreno del siguiente metro (1: Plano, 2: Rugoso): ");
        scanf("%d", &tipoTerreno);

        // Condicionales para el consumo de batería
        if (tipoTerreno == 1) {
            bateria -= 5;
        } else if (tipoTerreno == 2) {
            bateria -= 15;
        } else {
            printf("Terreno no reconocido. Penalizacion de consumo de energia.\n");
            bateria -= 20;
        }

        // El robot avanza 1 metro en cada iteración
        distanciaObjetivo--;
    }

    // Al salir del ciclo, verificamos por qué terminó
    if (distanciaObjetivo <= 0 && bateria >= 0) {
        return 1; // Éxito: llegó al objetivo con batería restante o en 0
    } else {
        return 0; // Fracaso: la batería bajó de 0 antes de llegar
    }
}

int main() {
    int distancia, bateriaInicial, resultado;

    printf("--- Simulacion de Mision de Exploracion ---\n");
    printf("Ingrese la distancia al objetivo (en metros): ");
    scanf("%d", &distancia);
    printf("Ingrese el nivel de bateria inicial (0-100): ");
    scanf("%d", &bateriaInicial);

    // Llamada a la función
    resultado = realizarMision(distancia, bateriaInicial);

    // Evaluación del valor de retorno
    if (resultado == 1) {
        printf("\nMision FINALIZADA: EXITO. El robot llego a su destino.\n");
    } else {
        printf("\nMision FINALIZADA: FRACASO. El robot se quedo sin energia en el camino.\n");
    }

    return 0;
}