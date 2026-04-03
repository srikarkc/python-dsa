class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x != 0:
            digit = x % 10

            if res > 214748364 or (res == 214748364 and digit > 7):
                return 0
            
            res = res * 10 + digit
            x //= 10

        return res * sign
