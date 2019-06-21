def hello(fun):
    print("Hello..")
    fun()

# fun has reference copy of bye
def bye():
    print("Bye..")

hello(bye)

