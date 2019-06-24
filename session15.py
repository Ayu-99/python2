print(">>App Started")

numbers = [1, 2, 3, 4, 5]
#a = 10; b=3; c=0
a = int(input("Enter a:"))
b = int(input("Enter b:"))
idx = int(input("Enter the index:"))
c = 0
#c = c//b  #Logical error as o/p is zero
#d = a//b
#print(d)
try:
    print(numbers[idx])
    print("c is:", c)
    d = a//b
    print(d)

#except IndexError as iRef:
    # iRef is the reference variable of object of class Index error which contains info of error occured
    # this object is created by virtual machine
 #   print("Some error occurred:", iRef)

#except ZeroDivisionError as dRef:
#    print("Some error occured:", dRef)

except Exception as iRef: # In this run-time polymorphism comes in action
        print("Some error occured:", iRef)

finally:
    print("This is Awesome !!")
# Finally will always run whether error occured or not, whether exception is handled or not

print(">>App Finished")
# Graceful/Normal Termination of Program
# In python, there is always run-time errors not compile-time errors
# in logical errors there will be no error but output will be wrong

# Abnormal Termination of Program / Run-Time Error
# Crash in Program- it degrades the performance of O.S

# designing the program in such a way that if error occurs then we can handle it so that Our prog DOES NOT
# CRASH

# Rest explanation see from github


# Priciple of RTP->Parent class Reference variable can point to child class objects