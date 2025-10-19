# Hash tables revision continue & 2 LC questions

## Questions

1. Meeting Rooms question

Mathematically, two intervals A and B overlap if:

`min(A.end, B.end) > max(A.start, B.start)`


## Important learning

Keys in dictionaries have O(1) lookup time NOT the values.

So, if you have 2 lists and you want to add all list1 values to a dictionary to take advantage of O(1) lookup.

### Doing it the wrong way

```python
def wrong_way(list1):
    my_dict = {}

    for i in enumerate(list1):
        my_dict[i[0]] = i[1]
```

The above code stores the index, list value in the dictionary but when you search values from the dictionary after, you will run O(n) if you have to go through all the values.

### Doing it the right way

```python
def right_way(list1):
    my_dict = {}

    for i in list1:
        my_dict[i] = True
```

Now, when you look for the values in the dictionary, you're only looking at the keys and that's O(1).

#### For the question about the repeating characters

You cannot just compare the adjacent characters!
