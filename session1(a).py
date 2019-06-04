johnsAge=30
print(johnsAge," ",hex(id(johnsAge)))

jenniesAge=30
print(jenniesAge," ",hex(id(jenniesAge)))

#copy operation:not data copy but reference copy(hash code copy)
jacksAge=johnsAge#johnsAge and jacksAge are pointing to same location
print(jacksAge," ",hex(id(jacksAge)))

del(johnsAge)
print(jenniesAge," ",hex(id(jenniesAge)))

#johnsAge and jenniesAge are called reference variables


