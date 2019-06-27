import numpy as np

# Explore: asarray vs array

arr = np.arange(10, 51, 3)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

# Access array elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[:3])
print(arr[3:])
print(arr[4:6])
print()

slices = slice(1, 20, 2)
print(slices)
print(arr[slices])

arr2D = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])
print(arr2D)
print("==============")
print(arr2D[0:2])
print("==============")
print(arr2D[0][1])
print("==============")
print(arr2D[0, 1])
print("==============")
print(arr2D[0:2, 0:2])
print()

arr3D = np.array([[(1, 2, 3), (4, 5, 6), (7, 8, 9)]])
print(arr3D)
print(arr3D[0][1])
print()
print(arr3D[:2])






