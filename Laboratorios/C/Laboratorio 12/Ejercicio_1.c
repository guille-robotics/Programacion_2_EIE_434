#include <stdio.h>

// ==========================================
// PROBLEMA 1: Firmware de Planta
// ==========================================

// Definición de la estructura (Plantilla de memoria)
typedef struct {
    int id;
    float nivel_actual;
    float capacidad_maxima;
    int valvula_abierta; // 0: Cerrada, 1: Abierta
} Estanque;

// Función de inicialización
void Estanque_init(Estanque* self, int id_asignado, float cap_max) {
    self->id = id_asignado;
    self->nivel_actual = 0.0;
    self->capacidad_maxima = cap_max;
    self->valvula_abierta = 0; 
}

// Función de control de llenado con lógica de seguridad
void Estanque_llenar(Estanque* self, float litros) {
    if (self->nivel_actual + litros > self->capacidad_maxima) {
        printf("\n[ALERTA] Riesgo de desbordamiento en Estanque %d. Operacion cancelada.\n", self->id);
        self->valvula_abierta = 0; // Estado seguro
    } else {
        self->valvula_abierta = 1; 
        self->nivel_actual += litros;
        printf("\n[OK] Inyectando %.2f L al Estanque %d. Nivel actual: %.2f L\n", litros, self->id, self->nivel_actual);
        self->valvula_abierta = 0; 
    }
}