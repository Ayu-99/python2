def addNumbers(num1, num2):
    sum = num1 + num2
    print("sum is:",sum)
    return None
    # automatically written none if we don not write

def addNumbersAgain(num1, num2):
    sum = num1 + num2
    return sum

addNumbers(10,20)

print(addNumbers(30,40))
print(addNumbersAgain(30,40))

print("sum of 30 and 40 is:",addNumbersAgain(30,40))
result = addNumbersAgain(30,40)
if result > 30:
    print("pass")
else:
    print("fail")


