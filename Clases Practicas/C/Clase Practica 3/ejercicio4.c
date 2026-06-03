#include <stdio.h>

/* * ROMPIENDO EL LÍMITE DEL RETURN:
 * La función es de tipo 'void' (no retorna nada usando la palabra return).
 * En su lugar, exige que le entreguemos dos direcciones de memoria (*dist_izq y *dist_der).
 */
void leer_sensores_distancia(float *dist_izq, float *dist_der) {
    
    /* * EL OPERADOR DE DESREFERENCIA (*):
     * Al colocar el asterisco antes del nombre del puntero, le estamos diciendo a C:
     * "No cambies la dirección, VIAJA a esa dirección y guarda este número allí".
     * Así, alteramos directamente la memoria del sistema.
     */
    *dist_izq = 12.5; 
    *dist_der = 8.3;
}

int main() {
    // 1. Declaramos las variables locales en el main y las inicializamos en 0
    float sensor_izquierdo = 0.0;
    float sensor_derecho = 0.0;
    
    /* * 2. LA LLAMADA:
     * Usamos '&' para enviar la "llave" de nuestras variables.
     * La función viajará hasta aquí y pondrá los nuevos valores directamente 
     * en los casilleros de 'sensor_izquierdo' y 'sensor_derecho'.
     */
    leer_sensores_distancia(&sensor_izquierdo, &sensor_derecho);
    
    // 3. Comprobamos que las variables fueron modificadas exitosamente
    printf("Lectura Custodio - Izq: %.2f cm, Der: %.2f cm\n", sensor_izquierdo, sensor_derecho);
    
    return 0;
}