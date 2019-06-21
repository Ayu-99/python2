import mysql.connector # used to connect python program to mysql database

class DBHelper:
    def saveCustomerInDB(self, customer):
        sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)

        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="AyuDB")
        # we can take any name in place of con
        cursor = con.cursor() #cursor is used to connect python file to my sql database
        cursor.execute(sql)
        con.commit() # it checks if any command between fails then it automatically fails all the commands
        # and there is no change in databases

        print(customer.name, " Saved !!")

    def updateCustomerInDB(self, customer):
        sql  ="update Customer  set name = '{}', email = '{}', phone = '{}' where cid = {}".format(customer.name, customer.phone, customer.email, customer.cid )
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="AyuDB")
        # we can take any name in place of con
        cursor = con.cursor() #cursor is used to connect python file to my sql database
        cursor.execute(sql)
        con.commit() # it checks if any command between fails then it automatically fails all the commands
        # and there is no change in databases

        print(customer.name, " Updated !!")



    def deleteCustomerInDB(self, cid):
        sql  ="delete from Customer where cid = {} ".format( cid )
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="AyuDB")
        # we can take any name in place of con
        cursor = con.cursor() #cursor is used to connect python file to my sql database
        cursor.execute(sql)
        con.commit() # it checks if any command between fails then it automatically fails all the commands
        # and there is no change in databases

        print(cid, " Deleted !!")

    def fetchAllCustomers(self):
        sql = "select * from Customer order by name desc"
        #sql = "select * from Customer order by name asc"
        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "AyuDB")
        cursor = con.cursor()
        cursor.execute(sql)
        #con.commit()

        """
        rows = cursor.fetchone()
        print(rows)
        """

        rows = cursor.fetchall()

        for row in rows:
            print(row)  # returns list of tuples

    def fetchCustomer(self, cid):
        sql = "select * from Customer where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="AyuDB")
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchone()
        print(rows)


class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {}  Phone: {} Email: {}".format(self.name, self.phone, self.email))


print("Options:")
print("1.Create New Customer")
print("2.Update Customer")
print("3.Delete Customer")
print("4.View All Customers")
print("5.Fetch only one customer")

choice = int(input())
if choice == 1:
    c1 = Customer(None, None, None)
    c1.name = input("Enter name:")
    c1.phone = int(input("Enter phone:"))
    c1.email = input("Enter email:")

    c1.showCustomerDetails()

    save = input("Do u like to save the customer(yes/no) ??")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(c1)

elif choice == 2:
    c1 = Customer(None, None, None)
    c1.cid = int(input("Enter customer ID:"))
    # we need to know which customer should be updated
    print("Enter new details:>>>")
    c1.name = input("Enter name:")
    c1.phone = input("Enter phone:")
    c1.email = input("Enter email:")

    c1.showCustomerDetails()

    save = input("Do u like to update the customer(yes/no) ??")
    if save == "yes":
        db = DBHelper()
        db.updateCustomerInDB(c1)

elif choice == 3:
    cid = int(input("Enter cid to be deleted:"))  # if a cid is deleted then it does not mean that that cid will
    # be given to another customer(roll no of student is his also when he left the school . his rollno is not given
    # to another student
    delete = input("Do u like to delete the customer(yes/no) ??")
    if delete == "yes":
        db = DBHelper()
        db.deleteCustomerInDB(cid)

elif choice == 4:
    db = DBHelper()
    db.fetchAllCustomers()

elif choice == 5:
    db = DBHelper()
    cid = int(input("Enter the customer id:"))
    db.fetchCustomer(cid)




