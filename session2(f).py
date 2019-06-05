#controller
# Conditional Constructs
# where we wish to check some rules/constraints
total = 1

# Regular if-else
if total >= 500:
    print("Flat 40% off ") # pep( python

else:
    print("sorry no discounts")

# Ladder if-else
if total >=100 and total < 200: #testcases
    print("flat 20% off")
elif total >=200 and total < 500:
    print("flat 30% off")
elif total >= 500:
    print("flat 50% off")
else:
    print("please  add valuables of upto 100 for discounts")

# nested if-else
isInternetConnected = True
isGPSConnected=False

if isInternetConnected:
    print("you can browse Google maps")
    if(isGPSConnected):
        print("you can Navigate using Google maps")
    else:
        print("to use navigation using google maps enable gps")
else:
    print("please connect to internet and Try again")

# Execute same code Snippets by taking Amazon/whatsapp/zomato as your use case
