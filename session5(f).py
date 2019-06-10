# Variable arguments :*args | where which is a reference variable to a tuple
def addNumbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for i in args:
        sum = sum + i

    print(sum)

addNumbers(10, 20, 30, 40, 50)
addNumbers(10,20,30)
addNumbers(10,20,30,40,50,60)