# Return the total number of distinct ways

class Solution:
    def coin_change_2(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]
    
sol = Solution()
sol.coin_change_2(4, [1,2,3])
