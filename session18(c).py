import numpy as np
arr = np.loadtxt("data.txt", dtype=int)
print(arr)

# Detect which no. is there in data.txt

print("============")

arr = np.arange(10, 200, 10)
print(arr)
np.savetxt("arraydata.txt", arr)
print("=Data Written=")

print()
arr1 = np.loadtxt("arraydata.txt")
print(arr1)

np.savetxt("arraydata.txt", arr, fmt="%04d", delimiter=",")
print("Data written")

# nan-not a number

# see h.w from github