#include <stdio.h>

/* * 1. DEFINICIÓN DE LA ESTRUCTURA
 * Aquí creamos el "molde". Aún no ocupa espacio en la memoria RAM, 
 * solo le decimos a C cómo se verá una variable de tipo 'CamaraScouting'.
 */
struct CamaraScouting {
    char modelo[20];       // Arreglo de tamaño fijo para texto
    int distancia_focal;   // Variable entera
    int grabando;          // Variable entera usada como booleano (1 = True, 0 = False)
};

int main() {
    /* * 2. CREACIÓN E INICIALIZACIÓN
     * Al declarar 'camara_principal', C reserva la memoria necesaria.
     * Podemos inicializar todos sus valores en una sola línea usando llaves {}.
     * El orden de los datos debe coincidir exactamente con el molde de arriba.
     */
    struct CamaraScouting camara_principal = {"Canon EOS 200D", 300, 1};
    
    /*
     * 3. ACCESO A LOS MIEMBROS
     * Usamos el operador de punto (.) para entrar a la estructura y leer o
     * modificar el valor específico de uno de sus miembros.
     */
    printf("Equipo: %s\n", camara_principal.modelo);
    printf("Lente: %d mm\n", camara_principal.distancia_focal);
    
    // Evaluamos el estado usando el miembro 'grabando'
    if(camara_principal.grabando == 1) {
        printf("Estado: REC (Grabando)\n");
    } else {
        printf("Estado: STBY (En espera)\n");
    }
    
    return 0;
}