ages1=(10, 20, 30, 40, 50, 60)
ages2={10, 20, 30, 40, 50, 60}
ages3=[10, 20, 30, 40, 50, 60]
print(ages1, hex(id(ages1)), type(ages1))
#cannot be altered(constant) ,
#this is known as immutable

print(ages2, hex(id(ages2)), type(ages2))#unordered
print(ages3, hex(id(ages3)), type(ages3))#list can be appended

#Ps: Tuple is IMMUTABLE(READ ONLY)
#List is MUTABLE
#Set is MUTABLE AND UNORDERED DUE TO UNIQUENESS

print(ages1[0])

#h.w
#how we will read in set
#Draw mwmory representation


