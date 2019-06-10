def squareOfNum(num):
    print("hashcode of num: before",hex(id(num)))
    num = num * num
    print(">>num is:",num)
    print("hashcode of num after",hex(id(num)))


number = 11
print("number hashcode before:",hex(id(number)))
squareOfNum(number)
print("number is:",number)
print("number hashcode after:",hex(id(number)))
