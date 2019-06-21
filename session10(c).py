file = open("session10.py", "r") # open function makes an object of wrapper class and copy its hashcode in file variable
print(type(file))

fileContents = file.read()
print(type(fileContents))

print()

print(fileContents)

print(len(fileContents))

print("Re-reading the file")
# Re-read the file
#file = open("session10.py", "r")
fileContents = file.read()
print(fileContents)

#once  a file is  opened and read, we cannot re-reAD IT>>
# yOU NEED TO RE OPEN AND RE READ IT
# do h.w
