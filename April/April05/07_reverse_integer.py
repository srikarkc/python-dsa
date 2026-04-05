class Solution:
    def reverse_int(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x:
            digit = x % 10

            if res > (2 ** 31 - 1) // 10 or (
                res == (2 ** 31 - 1) // 10 and digit > 7
            ):
                return 0
            
            res = (res << 1) + digit

            x //= 10

        return sign * res
    