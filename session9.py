"""
    Inheritance: IS-A relationship | Generalisation

    Maruti suzuki Swift Dzire IS-A swift

    Amazon e-commerce example
    shoe, led, Mobile, etc,...

"""

""""
class Shoe:
    def __init__(self, pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size


    def updateShoeDetails(self,pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def showShoeDetails(self):
        print("pid is:",self.pid)
        print("name is:", self.name)
        print("price is:", self.price)
        print("brand is:", self.brand)
        print("color is:", self.color)
        print("size is:", self.size)


class Mobile:
    def __init__(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def updateMobileDetails(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def showMobileDetails(self):
        print("pid is:", self.pid)
        print("name is:", self.name)
        print("price is:", self.price)
        print("brand is:", self.brand)
        print("ram is:", self.ram)
        print("memory is:", self.memory)


class Led:
    def __init__(self, pid, name, price, brand, tech, ss):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.tech = tech
        self.ss = ss

    def updateLedDetails(self, pid, name, price, brand, tech, ss):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.tech = tech
        self.ss = ss

    def showLedDetails(self):
        print("pid is:", self.pid)
        print("name is:", self.name)
        print("price is:", self.price)
        print("brand is:", self.brand)
        print("tech is:", self.tech)
        print("ss is:", self.ss)



s1 = Shoe(101, "AlphaBounce", 122,"Addidas", "black", 9)
m1 = Mobile(102, "Iphone", 234, "Apple", 4, 128)
l1 = Led(301, "SAmsung ", 808888, "samm", "fhdf", 48)
s1.showShoeDetails()
m1.showMobileDetails()
l1.showLedDetails()

"""

#Generalisation helps in saving time i.e reduces code redundancy i.e repeating code and hepls in customization
#Common code is generalised as Product
#We want to generalize so as to customize
class Product:
    def __init__(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand


    def updateProductDetails(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand


    def showProductDetails(self):
        print("=====Product Details================")
        print("pid is:", self.pid)
        print("name is:", self.name)
        print("price is:", self.price)
        print("brand is:", self.brand)
        print("=======================")

class Shoe(Product): #IS-a relationship | shoes is a product | inheritance
    def __init__(self, color, size):

        self.color = color
        self.size = size


    def updateShoeDetails(self, color, size):

        self.color = color
        self.size = size

    def showShoeDetails(self):

        print("======================")
        print("color is:", self.color)
        print("size is:", self.size)


class Mobile(Product):
    def __init__( self, pid, name, price, brand, ram, memory):
        Product.__init__(self, pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    def updateMobileDetails(self,pid, name, price, brand,ram, memory):

        Product.updateProductDetails(self,pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    def showProductDetails(self):
        Product.showProductDetails(self)

        print("====================")
        print("ram is:", self.ram)
        print("memory is:", self.memory)


class Led(Product):
    def __init__(self, tech, ss):

        self.tech = tech
        self.ss = ss

    def updateLedDetails(self,tech, ss):

        self.tech = tech
        self.ss = ss

    def showLedDetails(self):

        print("=====================")
        print("tech is:", self.tech)
        print("ss is:", self.ss)


m1 = Mobile(123, "Samsung", 244, "Samm", 4 , 128)
m1.showProductDetails()


