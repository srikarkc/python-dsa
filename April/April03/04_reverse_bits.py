class Solution:
    def reverseBits(self, n):
        res = 0

        while n:
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1

        return res