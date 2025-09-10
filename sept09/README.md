# Day 4 - Just revisiting Linked Lists

Don't use the following loop

```python
temp = self.head
for i in range(self.length - 1):
    temp = temp.next
```

Instead use

```python
temp = self.head
while temp.next is not self.tail:
    temp = temp.next
```