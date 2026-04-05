class Solution:
    def reverse_bits(self, n):
        res = 0

        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1

        return res