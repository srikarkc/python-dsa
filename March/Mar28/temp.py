my_dict = {
    "first_list": ["hello", "there"],
    "second_list": 1,
    "third_list": {
        "num": 1,
        "word": "awesome"
    }
}

print(my_dict.items())

for key, value in my_dict.items():
    print(key, value)