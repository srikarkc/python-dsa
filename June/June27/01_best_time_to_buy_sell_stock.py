class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = float("inf")

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
            
        return maxProfit
    