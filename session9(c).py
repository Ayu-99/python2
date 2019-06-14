#Class and Object Relationship
""""
class CA:
    num = 10

    def __init__(self):
        self.a  =102
    def show(self):
        print("num is:",self.num)
        print("a is:",ca.a)

ca = CA()
ca.show()

#Rule: Property of class can be accessed by classname,object or reference variable of object i.i self
#But property of object cannot be accessed by  class name
"""
class CA:
    num = 101

    def __init__(self):
        self.num =102
    def show(self):
        print("num  of object is:",self.num)
        print("num of class is:",CA.num)

ca = CA()
ca.show()

#if object has the variable then it does not take from parent class
# if it does not have then only it takes from parent
