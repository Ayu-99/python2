# re is regular expression (extract string from string)
import re
quote = "Search the candle rather than cursing the Darkness"
#result = re.match("candle", quote)   # match from starting
result = re.search("the", quote)  # gives only first 'the'
result = re.findall("the", quote)

print(result)
print(type(result))

data = re.split("the", quote)
print(data)

data = re.sub("the", "a", quote)
print(data)
print(quote)  #  original string does not change