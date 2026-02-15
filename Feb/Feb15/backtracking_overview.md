# Backtracking

Try a choice -> explore -> undo the choice -> try another choice

Backtracing template:

```python
def backtrack(path, choices):
    if goal reached:
        save path
        return

    for choice in choices:
        make choice
        backtrack(updated path, remaining choices)
        undo choice
```

## Problem 8 - Palindrome Partitioning

This problem and problem 9 - you create a res array and a path array initially.

1. state: start (where we are in the string), path(current condition)
2. base case: if start == len(s) - we used the whole string (save path)
3. choices - all end positions from start to n - 1

## Problem 9 - Letter combinations of a Phone Number

Let's use 'i' to hold state - indicating the digit that we're on.

Base case --> i == len(digits) - then the path is a full combo so save it.

choices -> digits[i]

## Problem 10 - n queens

Place exactly 1 queen per row.

At row r, try each column 'c': if (r, c) is safe -> place queen -> recurse to r + 1

Then, remove queen (backtrack)

What makes a spot unsafe?

If any of these already used: col = c, diag = r - c, antidiag = r + c

Squares on the same diagnol share the same r - c

Squares on the same antidiagnol share the same r + c
