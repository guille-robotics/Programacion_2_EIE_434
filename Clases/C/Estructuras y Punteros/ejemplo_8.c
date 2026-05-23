// Ejemplo 8: Simulación de un robot moviéndose en un plano (demuestra el uso de punteros, 
// que solucoinan el poder returnar mas de un valor a la vez, y el paso de parametros por referencia)
#include <stdio.h>
#include <unistd.h> // Para usar la pausa sleep()

// La funcion no "retorna" nada, modifica la memoria directamente
void obtener_coordenadas_robot(float *x, float *y, int t) {
    *x = 120.5 + (t * 2.5); // Simulamos movimiento en X
    *y = -45.2 - (t * 1.2); // Simulamos movimiento en Y
}

int main() {
    float latitud = 0.0, longitud = 0.0;
    
    // El ciclo va en el main para controlar el tiempo real
    for(int tiempo = 0; tiempo <= 5; tiempo++) {
        
        // Le entregamos las direcciones en cada iteracion
        obtener_coordenadas_robot(&latitud, &longitud, tiempo);
        
        printf("T=%ds -> Posicion: X=%.2f, Y=%.2f\n", tiempo, latitud, longitud);
        sleep(1); // Pausa de 1 segundo entre lecturas
    }
    
    return 0;
}