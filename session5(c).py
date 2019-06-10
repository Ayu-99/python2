def hello(name):
    print("hello",name)


print(hello)
print(hex(id(hello)))
hello("Ayushi")  # Execution

hi = hello  # reference copy || alias of hello
# this we do for eg->if we have two function pay(user) and payement(developer) ,then some security is there

print(hi)
print(hex(id(hi)))  # have same hashcode as hello
hi("Fionna")  # Execution






