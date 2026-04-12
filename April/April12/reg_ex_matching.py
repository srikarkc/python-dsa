class Solution:
    def reg_ex(self, s, p):
        memo = {}

        def dp(i, j):
            if (s, p) in memo:
                return memo[(s, p)]
            
            if j == len(p):
                return i == len(s)
            
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                answer = dp(i, j + 1) or (first_match and dp(i + 1, j))
            else:
                answer = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = answer
            return answer
        
        return dp(0, 0)
    