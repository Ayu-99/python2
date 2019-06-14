class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Parent constructor executed")


    def  showDetails(self):
        print("Hello, {} {}".format(self.fname, self.lname))


class Child(Parent): # relationship IS-A
    pass


print(Parent.__dict__)
print(Child.__dict__)

ch = Child("John", "Watson") #child can access parent class methods but it does not has parent class methods . tis can be verified by using dict with class child
print(ch.__dict__)

ch.showDetails()

# Rule1 :Whatsoever is in parent is accessible to child if not available in child