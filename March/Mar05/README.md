# Dynamic Programming 1-D

1 - Climbing stairs problem

Each move you can either climb 1 step or 2 steps. How many distinct ways can you reach the top?

dp[i] = # of ways to get to step i

dp[i] = dp[i - 1] + dp[i - 2]

Base cases --> dp[0] = 1 & dp[1] = 1

In the space-optimized solution, we only go for range(n) - this is because we take 'n' Fibonacci steps ahead.

```python
def climbStairs(n):
    a, b = 1, 1

    for _ in range(n):
        a, b = b, a + b

    return a
```
