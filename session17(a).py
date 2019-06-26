import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
#arr3 = np.array([[[], []]])

print(arr1)
print()
print(arr2)

print(len(arr1))
print(len(arr2))

print(arr1[1])
print(arr2[1][2])

print("arr1 shape is:", arr1.shape)
print("arr2 shape is:", arr2.shape)
print("arr2[0] shape is", arr2[0].shape)

#if arr2 is not symmetric then itwill print numpy array of list

print()
#a1 = np.zeros(8)
#print(a1)

a1 = np.ones(8)
print(a1)

print(a1.shape)

a2 = a1.reshape(2,2,2)
print(a2)

# Create a chessBoard of 8 x 8 with 1s and 0s

a3 = a2.ravel()
print(a3)