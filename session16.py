import json
# Java Script Object Notation

employee = {"eid":101, "name":"John", "salary":30000}
print(employee)
print(type(employee))

# Json -> string representation of dictionary

print()

# Convert Dictionary into JSON
# JSON is a textual i.e String representation of a Dictionary
# dumps fnc converts dict to string(JSON)


jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))
print()  # o/p in double quotes
""""
jsonData = str(employee)
print(jsonData)
print(type(jsonData))  # o/p in single quote
"""
# Get the JSON data i.e string format of dictionary
# and convert it into Dictionary


dictData = json.loads(jsonData)
print(dictData)
print(type(dictData))

# str cannot be converted back to dict
#print(dictData['status'])

