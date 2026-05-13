def procesar_lectura_sensor(valor_pwm):
    # Verificamos que el valor PWM este en el rango valido (0 - 255)
    # Si no lo esta, el programa se detiene con el mensaje indicado
    assert 0 <= valor_pwm <= 255, "Error: El valor PWM esta fuera de rango"
    
    # Si la asercion pasa, continuamos el procesamiento
    voltaje = (valor_pwm / 255.0) * 3.3
    return voltaje

# Esto funcionara bien
print(procesar_lectura_sensor(128))

# Esto lanzara un AssertionError y detendra el programa
print(procesar_lectura_sensor(300))