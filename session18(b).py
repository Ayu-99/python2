import numpy as np
arr1 = np.array([(8, 9), (10, 12), (13, 14)])
print(arr1[0:2, 1])

arr2 = np.array([10, 20, 30])
print(arr2.max())
print(arr2.min())
print(arr2.sum())
print()

arr3 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr3.sum(axis=1))
print()

arr4 = np.array([(4, 9, 16), (11, 13, 15)])
print(np.sqrt(arr4))
print(np.std(arr4))
print()

arr5 = np.array([(1, 2, 3), (3, 4, 5)])
arr6 = np.array([(1, 2, 3), (3, 4, 5)])

print(arr5 + arr6)
print()
print(arr5 - arr6)
print()
print(arr5 * arr6)
print()
print(arr5 / arr6)
print()
print(arr5 // arr6)
print("==================")

X = np.array([(1, 2, 3), (4, 5, 6)])
Y = np.array([(1, 2, 3), (4, 5, 6)])
print(np.vstack((X, Y)))
print()
print(np.hstack((X, Y)))
print("==================")

# Explore on numpy.org

Z = np.arange(0, 21, 3)
print(np.sin(Z))
print()
print(np.log10(Z))




