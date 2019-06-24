import os


print(os.getcwd())
print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDirectory = "/home/ayushi/PycharmProjects/python2"
pathToFile = "/home/ayushi/PycharmProjects/python2/session2"
print("Is python2 available:", os.path.exists(pathToDirectory))

#path = "/home/ayushi/PycharmProjects/python2/python3"
#print("Is python2 available:", os.path.exists(path))
#os.mkdir(path)
#print("Is python2 available:", os.path.exists(path))

# See h.w


