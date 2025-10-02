# Introduction

O - Omicron - always the worst case scenario

A single simple for loop will be O(n).

```python
for i in range(n):
    print(i)
```

1. Drop constants --> O(2n) becomes O(n)
2. Drop non-dominants --> O(n^2) + O(n) becomes O(n^2)

O(1) means 1 operation aka 'constant time'

O(log n) - Whenever you have binary search or are splitting in half

If you have different ranges - you cannot simplify it down to n

```python
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)
```

The above can only be simplfied to O(a * b)

