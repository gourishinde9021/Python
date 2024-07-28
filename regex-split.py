import re

text = "banana,mango,chikoo,pineapple,apple,orange"
pattern = ","

split_result = re.split(pattern,text)

print("Split result is", split_result)

li = text.split(",")
print(li)

mystring1 = "Thisismystring"
print(mystring1[0:4])
print(mystring1[::-1])

