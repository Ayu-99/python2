import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {}  Phone: {} Email: {}".format(self.name, self.phone, self.email))


# Use a service account
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

cRef = Customer("Fionna", "+91 99999 88888", "fionna@example.com")
data = cRef.__dict__

db.collection("Customer").document().set(data)
print(">> ", cRef.name, "Saved in Firebase")
