def squareOfNumber(num=1):
    return num*num

lRef = lambda num=1: num*num

numbers = [10, 11, 12, 15, 21]

#result = map(squareOfNumber, numbers)# build in fnc
result = map(lRef, numbers)
print(result)
print(list(result))

L1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lm1 = lambda n: n%2==0
result = map(lm1, L1)
print(list(result))


L1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lm1 = lambda n: n%2==0
result = filter(lm1, L1) # filter data on basis of true and false
print(list(result))

X = [10, 20, 30, 40, 50, 60]
Y = [11, 22, 33 ,44, 55]

lm2 = lambda P,Q :P+Q
result = map(lm2, X, Y)
print(list(result))

punjabPopulation = [12151, 234121, 564223, 763441, 54542]

from functools import reduce

result = reduce(lm2, punjabPopulation)
print("Total population is:", result)

# Explore the same with other sequences



