class Solution:
    def reverseInteger(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x != 0:
            digit = x % 10

            if res > (2 ** 31 - 1) or (res == 2 ** 31 - 1 and digit > 7):
                return 0
            
            res = (res * 10) + digit

            x //= 10

        return sign * res
    