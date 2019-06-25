# Importing Python Module

#import session16d
#import session16d as ss
#from session16d import hello,bye

# Importing file in another Python Package
# import db.DBHelper where db is name of package and DbHelper is name of file in db
# from db import DBHelper
from session16d import *

""""
session16d.hello("John")

e = session16d.Employee(101, "Fionna", 123456)
e.showEmployee()

"""

hello("John")

e = Employee(101, "Fionna", 123456)
e.showEmployee()
