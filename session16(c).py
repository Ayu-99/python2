import re

quote = "WOrk hard and get luckier"
data = re.findall(".", quote)  # . means character
print(data)

data = re.findall("\w", quote)
print(data)  # character without space

data = re.findall("\w*", quote)
print(data) #  words comes and with space

data = re.findall("\w+", quote)
print(data)  #  words but space eliminated

# Assignment -> Validate Vehicle number
# Vehicle ="PB10AB1234"

