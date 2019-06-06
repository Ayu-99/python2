technologies = ["ai", "android", "hadoop", "jee"]
technologies[1]="mobile apps" #update/set operation in lists
print(technologies)

print()

del technologies[2]

print(technologies)
print(technologies[2])

#print(technologies[0:2])
print(technologies[-1])
#print([-1:2])

data = [1, 2, 3, 4, 5, "john", "jennie", 'jim', "jack", "john", "joe"]
data.pop(3) # removes on the basis of index... 3 is index
print(data)


data.remove(3) # removes the matching element ...3 is data
print(data)

data.remove("john")
print(data)





