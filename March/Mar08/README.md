# Decode ways problem

Don't worry about converting the numbers in this problem into actual strings.

The question only asks for the number of ways to decode.

## Dynamic Programming Solution

dp[i] can be defined here as the number of ways to decode the first 'i' characters.

```python
dp[0] = 0

if dp[i] != 0:
    dp[i] += dp[i - 1]

if 10 <= int(s[i - 2:i]) <= 26:
    dp[i] += dp[i - 2]
```

Suppose: s = "226"

Define: dp[i] = number of ways to decode s[:i]

So:

dp[0] = ways to decode ""

`dp[0] = 1`

Why 1?

Because there is exactly one way to decode nothing: do nothing.

This sounds weird, but it makes the recurrence work.

dp[1] = ways to decode "2"

i = 1

Prefix is "2"

one-digit: "2" is valid → add dp[0] = 1

two-digit: not possible yet

`dp[1] = 1`

dp[2] = ways to decode "22"

i = 2

Prefix is "22"

one-digit: "2" is valid → add dp[1] = 1

two-digit: "22" is valid → add dp[0] = 1

`dp[2] = 2`

dp[3] = ways to decode "226"

Prefix is "226"

one-digit: "6" is valid → add dp[2] = 2

two-digit: "26" is valid → add dp[1] = 1

`dp[3] = 3`
