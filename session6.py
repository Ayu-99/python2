num = 10
def show():
    global num  # num be the variable in main frame . no need to make a new variable in show frmae
    #  global is used so that we can read and write the data of main frame
    num=11
    num=num%3
    print(">>1.num is:",num)

show()
print(">>2.num is:",num)


age = 20

cart = []

def addProductToCart(product):
    global cart
    cart.append(product)

