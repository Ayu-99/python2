data = ["c++", "java", "python", 90, 80, 90]
length = len(data)
print(length)
print(len(data))

x=[1,2,3,4]
print(max(x))
print(min(x))


y=["dev", "b", "ayu"]
print(max(y))
print(min(y))

# we cannot perform max and min operations on heterogeneous containers

print()

#iterate in list
for i in range(len(data)):
    print(data[i])

print("======")

# enhanced for loop/ for-each loop
for elem in data:
    print(elem)

print("=======")

print([j**2 for j in x]) #list comprehension


numbers= list(range(1,101))
print(numbers)

print([j%2==0 for j in x])
print([j for j in x if j%2==0])







