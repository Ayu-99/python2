"""
    h.w
    1.order can have many food items
    with user input create a small program
    with user input add as many food items in list called cart
    Create a function in order class ->getTotalAmount() which return total
    Create a function applyPromoCode in order class -> applyPromoCode
    Create a function showing sorted food items based on price of food items



"""
class Order:
    def __init__(self, oid, price, restName):
        self.oid = oid   # public
        self._price = price   # protected request not to use it but can be accesses
        self.__restName = restName  # private  cannot be accesssed but ca be with class name

    def __showOrder(self):
        print(self.oid,self._price,self.__restName)


o1 = Order(101, 3000, "ABc MAsala")
#print(o1.__dict__)
#print(o1.oid)
#print(o1._price)
#print(o1._Order__restName)
o1._Order__showOrder() # name mangling(writing classs name)
print(o1.__dict__)
print(Order.__dict__)

# Sorting Algorithms
# Gfg implement different algorithms on list


