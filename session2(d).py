# Bitwise Operators

a=8  # 0 0 0 0 1 0 0 0
b=12  # 0 0 0 0 1 1 0 0
c = a & b
d = a | b
e = a ^ b
print(c)
print(d)
print(e)

""""
x = 12
y = 3
z = x >> y # Right Shift Operation
print(z) # 1 1 0 0 >> 3 -> 0 0 0 1
z = x << y
print(z) # 1 1 0 0 << 3 -> 1 1 0 0 0 0 0
"""

x = -11
y = 2
z = x >> y

print("z is:",z)

