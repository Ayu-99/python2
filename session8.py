class Product:
    restaurantName = "ABC"

    #Constructor
    def __init__(self,name, price):
        self.name = name
        self.price = price

    #Function
    def showPrice(self):
        print(self.name, self.price, Product.restaurantName)

    #Destructor this will be executed when object will be deleted from memory
    def __del__(self):
        print("Product Deleted",self)

        #if we want to display a msg at the time of deletion of object then we use destructor
        #otherwise if we do not  write destructor , the also object will be deleted

p1 = Product("paneer",150)
p2 = Product("dal",200)


p1.showPrice()
p2.showPrice()

print(p1.__dict__)
print(p2.__dict__)
print(Product.__dict__)


print(hex(id(p1)))
print(hex(id(p2)))

#del p1