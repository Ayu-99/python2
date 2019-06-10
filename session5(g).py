# Keyword arguments which is **kwargs represent a dictionary
def  marks(**kwargs):  #  kwargs basically a dictionary(key has to be string) value can be any type
    print(kwargs)
    print(type(kwargs))

marks(physics=90, maths=92, chemistry=70)

def fun(*a, **b):
    print(a)
    print(b)

fun(10, 20, 30, a=10, b=20, c=30)



