# Number of One Bits

This problem can be solved very easily with built-in tools.

```python
class Solution:
    def hammingWeight(self, n):
        return bin(n).count("1")
```

The above solution might not be accepted.
