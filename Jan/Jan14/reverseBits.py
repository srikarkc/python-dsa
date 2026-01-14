# Given 32-bit unsigned int 'n' - reverse the bits of the binary representation

class Solution:
    def reverseBits(self, n):
        res = 0

        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1

        return res