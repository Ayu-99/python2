# session important in view of interview
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # If u wish to have more different ways other than __init
    # We can create methods of our own choice
    @classmethod # Known as Decorator
    def createPoint(cls, data):  # cls ->reference variable to the class
        points = data.split(",")
        # cls makes init to work
        refToObj = cls(int(points[0]), int(points[1]))
        return refToObj  # hashcode of object created returning to p3

    def showPoint(self):
        print("Point is:", self.x, self.y)

    @staticmethod # Decorator
    def greet(name):
        print("Hello ", name)

    @staticmethod
    def check(i1, i2):
        return i1>i2




p1 = Point()
p2 = Point(10, 20)

p1.showPoint()
p2.showPoint()

file = open("points.txt.py", "r")
data = file.readline()
print(data)

""""
points = data.split(",")
print(points[0], points[1])

print(type(points[0]), type(points[1]))


p3 = Point(int(points[0]), int(points[1]))
"""
p3 = Point.createPoint(data)
p3.showPoint()

print("Greater is :",Point.check(p3.x, p3.y))

Point.greet("Ayushi")


