cppCode = """
#include<iostream>
int main(){
cout<<"Hello";
return 0;
}
"""
print(cppCode)
print(type(cppCode))

file = open("/home/ayushi/Downloads/MyApp.cpp", "w")
file.write(cppCode)
#print(file)


file.close()

print(">>Cpp code written")

#switch case and ladderifelse why not in python and which is better
# 10 diff compuetr prog lang
# Ruby,dart,kotlin,scala,js,Go
# P.s-> if u can use inheritance RTP that will be more effective




