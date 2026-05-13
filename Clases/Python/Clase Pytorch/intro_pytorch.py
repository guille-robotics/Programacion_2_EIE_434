import torch
import numpy as np


#Creacion de un tensor directamente desde una lista de Python
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"Data Tensor: \n {x_data} \n")

#Creacion de un tensor a partir de un array de NumPy
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"NumPy Tensor: \n {x_np} \n")

#Creacion de un tensor con las mismas propiedades que otro tensor
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

#Creacion de tensores con formas específicas

shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")