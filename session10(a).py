"""
    Inheritance types:
    1. Single Level
    2. Multi level
    3. Hierarchy
    4. Multiple
    5. Hybrid

    Zomato - 1 to 4

"""
#Single Level
class A:
    pass

class B(A):
    pass
# Multilevel
class C(B):
    pass
# Hierarchy
class D(A):
    pass

# Multiple
class E:
    pass

class E(A):
    pass

class F(A, E):
    pass

# Hybrid
class G(F):
    pass


"""
payment options -Hierarchy
mulitple - promocode + total without promo
single- one restaurant and multiple items
multilevel - Not correct with extra toppings in dominoes pizza

protected and private
_ __

"""
