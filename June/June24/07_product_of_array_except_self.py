class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        prefix, postfix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        print(prefix)

        for i in range(n - 2 , -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        print(postfix)

        for i in range(n):
            res[i] = prefix[i] * postfix[i]

        return res
    
nums = [-1,0,1,2,3]
sol = Solution()
sol.productExceptSelf(nums)