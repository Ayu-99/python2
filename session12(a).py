
from tkinter import *

# import Session12
from session12 import Customer
from session12 import DBHelper

#from Session12 import *

# cRef = Session12.Customer("John", "+91 99999 88888", "john@example.com")
# cRef.showCustomerDetails()



def onClick():
    print("Button Clicked")

    cRef = Customer(None, None, None)
    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()
    cRef.showCustomerDetails()

    db = DBHelper()
    db.saveCustomerInDB(cRef)


window = Tk()

lblTitle = Label(window, text="Add Customer Details")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

window.mainloop() # Keep on running the program/process
