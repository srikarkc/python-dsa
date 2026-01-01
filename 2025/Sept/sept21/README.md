# Today is supposed to be revision day but I'm keen on learning about hash tables

A dictionary is a built-in python provided hash map.

We will build our own.

Prime numbers are preferred for the length of the hash map.

### Important to remember the hash function

```python
my_hash = 0
for letter in key:
    my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
```

## Big O for HashTable

1. Even though the worst case for get() is that all items are at one address O(n).

We assume that the hashing function does a decent job and the keys are spread evenly -> O(1).

2. Set operations and hashing method happen in constant time - O(1)

Note: Even though we loop through all the letters in the key for the hashing function.

We assume that the key length is small and bounded relative to the data size.

### Although insert and lookup are O(1) for hashtrees - that doesn't mean it is always better than a binary search tree. Binary search trees are sorted which makes them better for searching values that fall within a range.

Key lookup in a hash table is O(1) but the value lookup **is not** O(1). 
