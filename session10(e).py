file = open("session10.py", "r")
data = file.read(30)
print(data)

print("===========================")
data = file.read(60) # this will display characters after 30 to 60 as first 30 letters we have already read
print(data)

print("**************************")
data = file.read()
print(data)
print("*****************************")

print("Is file closed",file.closed)
file.close() # Explicitly close the file
print("Is file closed", file.closed)