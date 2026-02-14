class Solution:
    def generateParentheses(self, n):
        res = []

        def backtrack(open_used, close_used, path):
            if open_used == close_used == n:
                res.append("".join(path))
                return

            # option 1: add "("
            if open_used < n:
                path.append("(")
                backtrack(open_used + 1, close_used, path)
                path.pop()
            
            # option 2: add ")"
            if close_used < open_used:
                path.append(")")
                backtrack(open_used, close_used + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res