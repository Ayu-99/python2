def applyPromoCode(code, amount):
    if code == "FLAT50":
        discount = amount*(50/100)
        print("please pay:>>",amount - discount)

    elif code == "FLAT30":
        discount = amount*(30/100)
        print("please pay:>>",amount-discount)
    elif code == "FLAT10":
        discount = amount * (10 / 100)
        print("please pay:>>", amount - discount)

    else:
        print("no discounts")


def getDiscount(code, amount):
    discount = 0.0
    if code == "FLAT50":
        discount = amount*(50/100)
        #print("please pay:>>",amount - discount)

    elif code == "FLAT30":
        discount = amount*(30/100)
        #print("please pay:>>",amount-discount)
    elif code == "FLAT10":
        discount = amount * (10 / 100)
        #print("please pay:>>", amount - discount)

    else:
        discount = 0
    return discount # return takes control from function to position where u have called the function
# anything return after return will not be executed
    print("bye")




totalBill = 1000
#applyPromoCode("FLAT70",totalBill)
disc = getDiscount("FLAT50",1000)
print("discount is>>>",disc)
print("please pay>>",totalBill-disc)
