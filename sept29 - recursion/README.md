# Recursion

Base case and recursion case.

Think of a gift box that might either have a gift box or ball.

```python
def open_gift_box():
    if ball:
        return True
    open_gift_box()
```

Make sure the `if` statement evaluates to true (*might get complicated*). 

Make sure you return something when the `if` case is True.

## Call Stack

