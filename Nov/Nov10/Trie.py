# my_dict.setdefault(key, default_value)

person = {"Name": "Alice", "age": 25}

city = person.setdefault("city", "Toronto")

print(person)

# With setdefault - you never overwrite the existing value

city = person.setdefault("city", "Vancouver")

# --- 

node = node.children.setdefault(char, TrieNode())