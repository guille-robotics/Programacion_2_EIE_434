import torch

# 1. Definimos el dispositivo
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Trabajando con: {device}")

# 2. CREAMOS el tensor (Ahora si existe)
tensor = torch.ones(4, 4)

# 3. Ahora que existe, lo MOVEMOS al dispositivo
tensor = tensor.to(device)

# --- OPERACIONES ---

# Indexación
# Cambiamos la segunda columna (indice 1) a ceros
tensor[:, 1] = 0
print(f"Tensor Indexado:\n{tensor}")

# Concatenación
# dim=1 significa pegar las columnas hacia el lado
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(f"Tensor Concatenado:\n{t1}")

# Multiplicación elemento a elemento
print(f"Multiplicacion (mul):\n{tensor.mul(tensor)}")
print(f"Multiplicacion (*):\n{tensor * tensor}")