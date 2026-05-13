import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# z = x * y + y^2
z = x * y + y**2

# --- INSPECCION DEL GRAFO ---
print(f"Valor de z: {z.item()}")

# Esto muestra la ultima operacion realizada (la suma)
print(f"Funcion principal (grad_fn): {z.grad_fn}") 

# Podemos ver que hay detras de esa suma (la multiplicacion y la potencia)
print(f"Receta de la suma: {z.grad_fn.next_functions}")

# Disparamos el calculo
z.backward()

print(f"dz/dx: {x.grad}") # 3.0
print(f"dz/dy: {y.grad}") # 8.0