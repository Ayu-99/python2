"""

        Relationship Mapping

        HAS-A relationship
        1 Engineer working on 1 project
        1 Engineer working on many projects
        Many engineers working on many projects

        1 customer has 1 address
        1 customer have many addreses
        many customers have many addresses

        1 image to one
        1 image to many
        many images to many

        sender
            size
            time
            dataSwitch

        reciever
            dataswitch



        1 dress to one
        1 dress to many
        many dresses to many


        customer
            name
            phone
            email
        address
            adrsLine
            city
            state
"""

class Customer:

    #Constructor for standarisation
    """def __init__(self, name, phone, email, addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses = addresses # HAS-A relationship (1 customer has many addresses)
        HAS-A realtionship(one-one)
    """

    def __init__(self, name, phone, email, addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses = addresses


    def updateCustomerDetails(self, name, phone, email,addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses = addresses
    def showCustomerDetails(self):

        print("========================")
        print("Name:\t",self.name)
        print("Phone:\t",self.phone)
        print("Email:\t",self.email)
        #print("Addresses:\t",self.addresses)

       # print(self.addresses.showAddressDetails()) # 1 - 1

        print("Address list for John:>>>>>>>")

        for adrs in self.addresses: # 1 - *(many)
            adrs.showAddressDetails()


        print("===================================")
class Address:

    # Constructor for standarisation
    def __init__(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    def showAddressDetails(self):
        print("========================")
        print("Adrsline:\t", self.adrsLine)
        print("City:\t", self.city)
        print("State:\t", self.state)
        print("=========================")


addrList=[]
choice = "yes"
while choice == "yes":
    addr=Address(None,None,None)
    addr.adrsLine=input("enter address ")
    addr.city = input("enter city")
    addr.state= input("enter state")
    addrList.append(addr)
    print("Do u want to enter another address??(yes/no)>>")
    choice = input()

""""
a1 = Address("Redwood lane", "ldh", "punjab")

a2 = Address("hellwood lane", "Chennai", "Tamil Nadu")


# List of addresses
addrList = [a1, a2]

#c1 = Customer("John",  "123456789", "Redwood@", a1)
c1 = Customer("John",  "123456789", "Redwood@", addrList)

c1.showCustomerDetails()

a1.showAddressDetails()

#cRef = c1
#cRef.showCustomerDetails()


"""

""""
a1 = Address(None, None, None)
a1.adrsLine = input("enter address:")
a1.city= input("enter city:")
a1.state=input("enter state:")

a2 = Address("hellwood lane", "Chennai", "Tamil Nadu")
"""

# List of addresses
#addrList = [a1, a2]

#c1 = Customer("John",  "123456789", "Redwood@", a1)
c1 = Customer("John",  "123456789", "Redwood@", addrList)

c1.showCustomerDetails()

#a1.showAddressDetails()

#cRef = c1
#cRef.showCustomerDetails()
