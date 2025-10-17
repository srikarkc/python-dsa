# Oct 16, 2025 - Thursday

1. Sort stack problem

2. Implement a queue with stacks

## Trees

A linked list is a tree that doesn't fork.

---

## @dataclass

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
```
