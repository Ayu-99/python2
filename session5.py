# Functions
"""
    f(x)=x*x
    f(2)=2*2 ->4

    Functions/methods/procedure in programming language
    Function contains instructions which shall be executed in a sequence

    why loops ?
    we use loops so that we can perform certain task again and again

    why Functions?
    Function can also be executed again and again but functions represent some task to be done again and agin which cannot be done using loops
    Modularization in our prog is achieved by using functions


    registerUser
    Functions:
    1.They have a name.eg->registerUser
    2.It may not have inputs.eg->registerUser(name,phone,email)
    3.It will have definition.eg->how name and phone email will be stored in database
    4.It may or may not have ack.eg->Giving a suitable msg to user like thank u



"""

""""
sender = "7837822348"
reciever = "9877205141"
amount = 500
senderBalance = 10000
recieverBalane = 5000
senderBalance = senderBalance - amount
recieverBalane = recieverBalane + amount
print("sender balance:>>",senderBalance)
print("reciever balance:>>",recieverBalane)
print(">>>Transaction done")

# this above code will do only one transaction

"""
def pay(sender, reciever, amount):
    print(sender,"has send ",amount,"to",reciever)


pay("9877205141", "7837822348", 10000)
pay("3216548772", "1234567891", 500)




def addNumbers(num1, num2):
    num3 = num1 + num2
    print(">> sum is:",num3)

addNumbers(10,20)
addNumbers(50,50)
addNumbers(-70,30)

