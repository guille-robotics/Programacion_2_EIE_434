#include <stdio.h> // Incluimos la librería estándar de entrada/salida para usar printf y scanf

int main() {
    // Declaración de variables:
    // 'n' almacenará el número ingresado por el usuario.
    // 'i' será nuestro contador para el ciclo iterativo.
    // 'es_primo' actúa como una variable "bandera" (flag) o booleana: 
    // Asumimos inicialmente que el número SÍ es primo (1 = Verdadero).
    // Si encontramos un divisor, cambiaremos esta bandera a 0 (Falso).
    int n, i, es_primo = 1;

    // Solicitamos al usuario que ingrese el dato
    printf("Ingrese un numero entero positivo: ");
    
    // Leemos el dato ingresado. 
    // Recuerda usar '&' antes de 'n' para pasar la dirección de memoria donde se guardará el valor.
    scanf("%d", &n);

    // --- CASOS ESPECIALES ---
    // Por definición matemática, los números 0 y 1 no se consideran números primos.
    // Si el usuario ingresa alguno de estos, bajamos la bandera inmediatamente.
    if (n == 0 || n == 1) {
        es_primo = 0; // 0 significa "Falso, no es primo"
    } 
    // --- CASO GENERAL ---
    else {
        // Un número es primo si solo es divisible por 1 y por sí mismo.
        // Por lo tanto, empezamos a buscar divisores desde el 2.
        // Optimización: No tiene sentido buscar divisores más allá de la mitad del número (n / 2),
        // ya que ningún número mayor a su mitad puede ser un divisor entero (excepto él mismo).
        for (i = 2; i <= n / 2; ++i) {
            
            // Usamos el operador módulo (%) que nos entrega el resto de una división.
            // Si el resto de dividir 'n' entre 'i' es exactamente 0, significa que 'i' es un divisor.
            if (n % i == 0) {
                // Como encontramos un divisor distinto de 1 y 'n', el número ya no puede ser primo.
                es_primo = 0; // Bajamos la bandera (Falso)
                
                // Optimización: Como ya sabemos que no es primo, no necesitamos seguir comprobando 
                // el resto de los números. Usamos 'break' para salir del ciclo 'for' inmediatamente.
                break;
            }
        }
    }

    // --- SALIDA DE RESULTADOS ---
    // Evaluamos el estado final de nuestra bandera 'es_primo'.
    // Si la bandera sigue en 1, significa que el ciclo nunca encontró un divisor.
    if (es_primo == 1) {
        printf("%d es un numero primo.\n", n);
    } else {
        // Si la bandera cambió a 0 en los casos especiales o dentro del ciclo, no es primo.
        printf("%d NO es un numero primo.\n", n);
    }

    // Indicamos que el programa finalizó correctamente
    return 0;
}