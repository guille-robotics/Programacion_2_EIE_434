#include <stdio.h>

// Función que genera la rampa de PWM
void generarRampaPWM(int velocidadInicial, int velocidadFinal, int paso) {
    printf("Generando rampa PWM de %d%% a %d%% con pasos de %d\n", velocidadInicial, velocidadFinal, paso);
    
    // Condicional inicial para saber si la rampa es ascendente o descendente
    if (velocidadInicial <= velocidadFinal) {
        // Rampa de aceleración
        for (int v = velocidadInicial; v <= velocidadFinal; v += paso) {
            int pwmSalida = v;
            
            // Condicional de seguridad (Clamp)
            if (pwmSalida > 100) pwmSalida = 100;
            if (pwmSalida < 0) pwmSalida = 0;
            
            printf("Señal PWM: %d%%\n", pwmSalida);
        }
    } else {
        // Rampa de desaceleración
        for (int v = velocidadInicial; v >= velocidadFinal; v -= paso) {
            int pwmSalida = v;
            
            // Condicional de seguridad (Clamp)
            if (pwmSalida > 100) pwmSalida = 100;
            if (pwmSalida < 0) pwmSalida = 0;
            
            printf("Señal PWM: %d%%\n", pwmSalida);
        }
    }
}

int main() {
    printf("--- Controlador de Rampa de Motor DC ---\n\n");
    
    printf("Prueba 1: Aceleracion rebasando limites (20 a 120, paso 15)\n");
    generarRampaPWM(20, 120, 15);
    
    printf("\nPrueba 2: Frenado brusco (80 a -10, paso 20)\n");
    generarRampaPWM(80, -10, 20);

    return 0;
}