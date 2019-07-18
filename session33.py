import torch
import torchvision
import numpy as np

# print(torch.__version__)
# print(torchvision.__version__)

X = torch.empty(5, 3)
print(X)
print(type(X))

X = torch.rand(3, 3)
print(X)

X = torch.zeros(5, 5, dtype=torch.int)
print(X)

print()

numbers = [10, 20, 30, 40, 50]
print(numbers)

torchTensor = torch.tensor(numbers)
print(torchTensor)

nArray = np.array(numbers)
print(nArray)

nArray = torchTensor.numpy()
print(nArray)

tArray = torch.from_numpy(nArray)
print(tArray)








