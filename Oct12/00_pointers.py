print("Demo - Integers are immutable")
num1 = 11

num2 = num1
# num1 and num2 point to the same address
print("num1 and num2 point to the same address")
print(id(num1))
print(id(num2))

num2 = 22

# num2 now points to another address
print("num2 now points to another address")
print(id(num2))
print(num2)
print(num1)


# Dictionary are mutable
print("\nDictionaries are mutable")

dict1 = {'value': 11}

print("Dictionaries point to the same address")
print(id(dict1))
print(dict1["value"])

dict2 = dict1

# dict2 points to the same address
print("Updating the value of dict2 changes dict1")
dict2['value'] = 22
print(id(dict2))
print(dict1["value"])