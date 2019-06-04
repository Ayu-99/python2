dishPrice=100
dishesPrices=100, 200, 350, 500, 120
dishesPrices=(100, 200, 350, 500, 120) #homogeneous multi value container


#the storage container we have made is of type int
print(dishPrice, hex(id(dishPrice)), type(dishPrice))

print(dishesPrices, hex(id(dishesPrices)), type(dishesPrices))

print(dishesPrices[0], hex(id(dishesPrices[0])), type(dishesPrices[0]))

dishesPrices=(100, 200.22, 350, 500, 120, "100") #heterogeneous multi- value container
print(dishesPrices)
print(type(dishesPrices[1]))
