from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("serviceKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {}  Phone: {} Email: {}".format(self.name, self.phone, self.email))


def onClick():
    print("Button CLicked!!")
    c1 = Customer(None, None, None)
    c1.name = entryName.get()
    c1.phone = entryEmail.get()
    c1.email = entryEmail.get()

    c1.showCustomerDetails()

    data = c1.__dict__
    print(data)
    db.collection("Customer").document().set(data)
    print(">> ", c1.name, "Saved in Firebase")
    print("Done")


def onClick2():
    print("Button Clicked")
    c1 = Customer(None, None, None)
    c1.id = entryId.get()
    c1.name = entryName.get()
    c1.phone = entryEmail.get()
    c1.email = entryEmail.get()

    c1.showCustomerDetails()

    data = c1.__dict__
    print(data)
    db.collection("Customer").document().set(data)
    print(">> ", c1.name, "Updated in Firebase")
    print("Done")



print("Enter ur choice:")
print("1.Save new Customer:")
print("2.Update the Customer:")
print("3.Delete a Customer:")
print("4.View all Customers:")

choice = int(input())

if choice == 1:
    window = Tk()
    title = Label(window, text="Add Customer Details>>")
    title.pack()

    name = Label(window, text="Add Customer Name:")
    name.pack()

    entryName = Entry(window)
    entryName.pack()


    phone = Label(window, text="Add Phone Of Customer:")
    phone.pack()

    entryPhone = Entry(window)
    entryPhone.pack()



    email = Label(window, text="Add Email Of Customer:")
    email.pack()

    entryEmail = Entry(window)
    entryEmail.pack()

    btnAddCustomer = Button(window, text="ADD CUSTOMER", command=onClick)
    btnAddCustomer.pack()

    window.mainloop()

elif choice == 2:

    window = Tk()

    id = Label(window, text="Enter the Customer id which is to be updated:")
    id.pack()

    entryId = Entry(window)
    entryId.pack()

    title = Label(window, text="Add the new Customer details:")
    title.pack()

    name = Label(window, text="Add the Customer Name:")
    name.pack()

    entryName = Entry(window)
    entryName.pack()

    phone = Label(window, text="Add Phone Of Customer:")
    phone.pack()

    entryPhone = Entry(window)
    entryPhone.pack()

    email = Label(window, text="Add Email Of Customer:")
    email.pack()

    entryEmail = Entry(window)
    entryEmail.pack()

    btnAddCustomer =  Button(window, text="UPDATE CUSTOMER", command=onClick2 )
    btnAddCustomer.pack()

    window.mainloop()


elif choice == 3:
    window = Tk()

    id = Label(window, text="Enter Customer ID to be deleted:")
    id.pack()

    entryId = Entry(window)
    entryId.pack()

    btnAddCustomer = Button(window, text="DELETE CUSTOMER", command=onClick3)
    btnAddCustomer.pack()

    window.mainloop()

elif choice == 4:
    window = Tk()
    title = Label(window, text="LIST OF ALL CUSTOMERS>>>")
    title.pack()

    btnAddCustomer = Button(window, text="VIEW ALL", command=onClick4)
    btnAddCustomer.pack()

    window.mainloop()



