#! /bin/usr/ env python
import numpy as np

arr1 = np.arange(10, 21)  # makes an array in this range
print(arr1)
print()

arr2 = np.arange(10, 31, 3)
print(arr2)
print()

arr3 = np.ones((3, 3), dtype=int)
print(arr3)
print()

arr4 = np.ones((3, 3, 3), dtype=int)
print(arr4)
print()

arr3[0][1] = 9
print(arr3)
print()

arr5 = np.linspace(0, 21, 4, dtype=int)
print(arr5)
print()




