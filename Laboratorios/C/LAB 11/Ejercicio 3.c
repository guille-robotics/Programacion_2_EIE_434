#include <stdio.h>

// 1. Definición de la estructura
struct Sensor {
    int id;
    float medicion;
};

int main() {
    // 2. Declaración de la variable tipo estructura
    struct Sensor mi_sensor;

    // 3. Asignación de valores
    mi_sensor.id = 1;
    mi_sensor.medicion = 25.5;

    // 4. Impresión de los datos
    printf("--- Datos del Equipo ---\n");
    printf("ID del sensor : %d\n", mi_sensor.id);
    printf("Medicion      : %.2f\n", mi_sensor.medicion);

    return 0;
}