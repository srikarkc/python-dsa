class Solution:
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF      # 32 bits all 1s
        MAX_INT = 0x7FFFFFFF   # largest positive 32-bit int

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # if a is negative in 32-bit signed form
        return a if a <= MAX_INT else ~(a ^ MASK)