"""
    Object oriented programming structure
    OOPS(industrial fit)
    used where requirements are not clear(easy to update)

    > Object
    > Class


    1.Encapsulation
    2.Abstraction
    3.Inheritance
    4.Polymorphism

    Realvworld:
    Object: is anything which you can see and touch
        which is real ->real time entity(sach much ki cheez)

    Class: is drawing of an object
            is representation how an object will look like

    what will you think of first??

    OOPS principle-
    1.Think of an object
    2.Draw object
    3.Create Real object by looking drawing

    Computer Science-
    Object - Multi value container

    # customization (my own multi value container ...if i want to make my own mvc having own properties
    #If we wish to customize mvc we will create Objects

    Class : is textual representation of an object

    eg: Geometry box

            ALL pencils(homo mvc)
            pencils,sharpner ,pen(hetero mvc)

            User is an object
            User has lot of data associated with it
                name
                phone
                email
                gender
                age
                address
                *
                **

                Identification of an object
                Requirement - User should register in my app,user should enter source and destination
                location and book a cab
                User should be allocated a driver to complete ride

                Model view controller
                Model -> object


                Driver ->object(name,phone,email,license,experience***)
                Cab->object(brand,type,colour,regNum***)
                Ride->object(source,dest,cab,driver,user)



                Data associated with objects is attributes


"""

class User:
    pass


class Driver:
    pass

data = []
print(type(data))

# 1. object construction statement
u = User()
d = Driver()
v = User()

# u and d are not objects they are reference variables to object
# object has hashcode not name
print(type(u))
print(type(d))
print(type(v))


print(u)
print(d)
print(v)

# 2. write data in object
u.name = "John"
u.phone = "7837822345"
u.email = "ayushisharma5141@gmail.com"

d.name = "George"
d.phone = "9877205416"
d.experience = 3
d.license = 34567

v.name = "fionna"
v.age = 24
v.salary = 20000

# reference copy
w = v

print(w)

# 3. Update operation
u.name = "john watson"
u.phone = "123456789"
v.age = 33
# w.age=33 same as v.age=33

# 4. Delete operation
del u.phone
del d.license


# 5. Read Operation on object
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)



