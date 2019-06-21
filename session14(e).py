# Nested Function/Local Function
def hello():
    print("Hello..")
    def bye():
        print("Bye..")

    print(bye)
    bye()

print(hello)
hello()



