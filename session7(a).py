Assignment:

class Product:
    count = 0
    def __init__(self):
        count = count + 1
    def showNumberOfObjects(self):
        print(count)

p1 = product()
p2 = product()
p3 = product()
p4 = p1
p5 = p3



p5.showNumberOfObjects()
# output should be_> Total Product Objects :?