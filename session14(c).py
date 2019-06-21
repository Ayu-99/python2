def hello():
    return "hello"

h = hello
print(h)
print(type(h))
print(hello())
print(h())

print("*******")

def helloAgain():
    yield "Hi"
    yield "Hello"
    yield  "Heva"
    yield "Namaste"

#Refernce Copy
ha = helloAgain
print(ha)  # Hashcode
print(type(ha)) # function
print(helloAgain()) # Execution of function which is yielding return Generator

gen = ha()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

