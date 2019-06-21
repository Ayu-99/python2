file = open("session10.py","r")
line = file.readline()
print(line)

line = file.readline()
print(line)

line = file.readline()
print(line)

line = file.readline()
print(line)

lines = file.readlines()
print(lines)
print(type(lines)) # List of all the lines in a file

for line in lines:
    print(line)


