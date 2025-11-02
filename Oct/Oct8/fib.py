counter = 0

memo = [None] * 10000

def fibonnaci(n):
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fibonnaci(n - 1) + fibonnaci(n - 2)
    return memo[n]

print(fibonnaci(999))