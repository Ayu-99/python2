import numpy as np
# numpy uses less memory and less time

# List Creation
numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

print()

array = np.array([1, 2, 3, 4, 5])
print(array, type(array))

print()

# Check size
print(len(array))

print()

# Update data in array
array[2] = 222

array2 = np.append(array, [11,23,13])
print(array2)

print()

# Iterate in array
for elem in array:
    print(elem)

print()


