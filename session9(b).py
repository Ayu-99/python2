class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Parent constructor executed")


    def  showDetails(self):
        print("Hello, {} {}".format(self.fname, self.lname))


class Child(Parent): # relationship IS-A
    def __init__(self, fname, lname, vehicle, salary):
        Parent.__init__(self, fname , lname)
        self.vehicle = vehicle
        self.salary = salary
        print("Child costructor executed")

    # Overriding
    def showDetails(self):
        Parent.showDetails(self)
        print("Hello,{} {} {} {}".format(self.fname, self.lname, self.vehicle, self.salary))
print(Parent.__dict__)
print(Child.__dict__)

ch = Child("John", "Watson",2,30000) #child can access parent class methods but it does not has parent class methods . tis can be verified by using dict with class child
print(ch.__dict__)



ch.showDetails()

#ch.show()

#in child to have customization , we shall access parents properties
# if same function with same name in child we call it overriding