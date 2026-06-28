class Solution:
    def maxProfit(self, prices):
        minPrice = float("inf")
        maxP = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxP = max(maxP, profit)

        return maxP
    