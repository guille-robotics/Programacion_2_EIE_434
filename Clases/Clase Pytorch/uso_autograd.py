import torch

# 1. Definimos un escalar x = 3.0
# El parametro requires_grad=True le indica a PyTorch que debe
# rastrear todas las operaciones que involucren a x.
x = torch.tensor(3.0, requires_grad=True)

# 2. Realizamos una operacion: y = x^2
y = x ** 2
print(f"Resultado de y: {y}") # Muestra 9.0 y el grad_fn (la receta de la derivada)

# 3. Calculamos los gradientes (Derivamos y con respecto a x)
# PyTorch aplica la Regla de la Cadena internamente.
y.backward()

# 4. Mostramos el resultado de la derivada en el punto x = 3
# Si y = x^2, entonces dy/dx = 2x. Para x=3, el resultado es 6.
print(f"El gradiente (derivada) en x=3 es: {x.grad}")