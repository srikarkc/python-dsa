def dfs(node):
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return max(left, right) + 1

def backtrack(i, path):
    if done_condition:
        ans.append(path[:]); return
    for choice in choices_from(i, path):
        path.append(choice)
        backtrack(next_i, path)
        path.pop()

def dfs(r, c):
    if out_of_bounds_or_water: return
    grid[r][c] = '0'
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dfs(r+dr, c+dc)

def myPow(x, n):
    if n == 0: return 1.0
    if n < 0: return 1.0 / myPow(x, -n)
    half = myPow(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x