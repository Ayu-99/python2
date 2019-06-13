"""
    Student
        name
        phone
        email
        password
        isCollegeTraining
        collegeName
        rollNum

"""
""""
class Student:
    pass

s1 = Student()
s1.name = "Ayushi"
s1.phone = 9877205141
s1.email = "ayushisharma5141@gmail.com"
s1.password = "pass123"
s1.isCollegeTaining = True
s1.collegeName= "abc name"
s1.rollNum = 23

print(s1.__dict__)

# challenge that there is no standarisation
# solution : Constructors

"""

class Student:

    schoolName = "ATPL"
    +-
    # __init__ is constructor . Constructor is property of class
    def __init__(self, name, phone, email, password, isCollegeTraining, collegeName, rollNum ):  # self in java and cpp is this
        # self is a reference variable which will hold hashcode of current object

        print("self is:",self)
        self.fullName=name
        self.phone=phone
        self.email = email
        self.password= password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum
        #left hand-property of object ... right hand property is of class

    # over-writing -A new constructor will be created and old will be removed

    #def __init__(self,name,phone):
    #    self.name = name
     #   self.phone=phone

    #showStudentDetails property of class
    def showStudentDetails(self):

        print("=========================")
        print("Details of ",self.fullName)
        print("Phone no:",self.phone)
        print("Rollno:",self.rollNum)
        print("========================")



s1 = Student("John",789456123,"john123","john",True,"ABC ",123)  # s1 will be copied into self
# Student.__init__(s1,)
print("s1 is:",s1)
s2 = Student("Fionna",123456789,"Fionna123","fionna",True,"DEF ",33)
print("s2 is:",s2)


#s3 = Student("ayushi",123456789)
s1.age = 22
s1.vehicleNum = 12345

s1.fullName="John watson"
s2.fullName="Fionna Flynn"

#del s1.age
#del s1.phone


s1.showStudentDetails()
s2.showStudentDetails()# Student.showStudentDetails(s1)
# so with the use of constructors we achieve standarisation and each attribute of diff objects have same name
print(s1.__dict__)
print(s2.__dict__)
print()
print(Student.__dict__)


