# List in Python
students = ["John", "Jennie", "Jim", "Jack", "Joe"]
print(students, type(students))

#1.conactenation
print(students + ["fionnas","george"])
print(students)
# original list will not be changed on concatenation... new list will be created ..
# no changes will be done on students

# 2.repitition
print(students*3)
print(students)

# 3.membership testing
print("John" in students)

# 4.indexing
print(students[2])

# 5.slicing
print(students[1:4])

