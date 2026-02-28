# setting default value to 0 and incrementing count by 1 in python

count = {}

for key in ["apple", "apple", "banana"]:
    count[key] = count.setdefault(key, 0) + 1

print(count)