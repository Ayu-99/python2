def areaOfCircle(radius = 2):
    area = 3.14*radius*radius
    return area

#
result = areaOfCircle(3.3)
print(result)

# Reference Copy
area = areaOfCircle
result = area(4.4)
print(result)

# Lambda ->question in interview
# is a function just like a regular function
# Rule: Lambdas can evaluate a single expressions
# Lambdas will have no name and shall return a reference
# Used to write the function in a single line

lm1 = lambda radius=2.2 : 3.14*radius*radius
lm2 = lambda x=1, y=2: x*y
print("Area of circle is:", lm1())
print("Area of circle with radius 5.5 is:", lm1(5.5))
print(lm2(2, 3))

# Lambda calculus
# aws lambda
