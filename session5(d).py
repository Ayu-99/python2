def hello():
    print("hello")

print("hello is:",hello)

#hi = hello

#  update operation : overwriting
def hello():
    print("bye")

print("hello now is",hello)
# if we again make the fnc of same name then that will have different hashcode

hi = hello
del hi

hello()

#hi()


