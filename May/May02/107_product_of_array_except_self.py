class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(n):
            result[n] = prefix[i] * postfix[i]

        return result
        