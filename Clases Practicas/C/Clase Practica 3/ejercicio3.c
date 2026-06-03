#include <stdio.h>

struct CajaYOLO {
    float x;
    float y;
    float ancho;
    float alto;
};

/* * PASO POR REFERENCIA:
 * Observa el asterisco (*caja). La función no recibe una COPIA de la estructura.
 * Recibe la DIRECCIÓN DE MEMORIA de la estructura original que vive en el main.
 * Esto es vital en la industria: ahorra memoria y tiempo de procesamiento.
 */
void escalar_caja(struct CajaYOLO *caja, float factor) {
    /*
     * EL OPERADOR FLECHA (->):
     * Como 'caja' es un puntero (una dirección), no podemos usar el punto (.)
     * directamente. Primero debemos "viajar" a la dirección y luego acceder al dato.
     * C inventó el operador '->' para hacer ambas cosas a la vez:
     * caja->ancho es exactamente lo mismo que hacer (*caja).ancho
     */
    caja->ancho = caja->ancho * factor;
    caja->alto = caja->alto * factor;
}

int main() {
    // Variable original creada en la función main
    struct CajaYOLO deteccion = {100.0, 150.0, 50.0, 80.0};
    
    printf("Tamaño original: %.2f x %.2f\n", deteccion.ancho, deteccion.alto);
    
    /*
     * OPERADOR DE DIRECCIÓN (&):
     * Le enviamos a la función "dónde está" la variable, no la variable en sí.
     */
    escalar_caja(&deteccion, 1.5);
    
    // Al imprimir, veremos que la función logró alterar nuestra variable original
    printf("Tamaño escalado: %.2f x %.2f\n", deteccion.ancho, deteccion.alto);
    
    return 0;
}