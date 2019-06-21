def dataGenerator():
    file = open("session14.py", "r")
    lines = file.readlines()  # List made of lines
    for line in lines:
        yield line

# A fnc which yields upon execution creates a generator object
dg = dataGenerator()
print(dg)
print(next(dg))

