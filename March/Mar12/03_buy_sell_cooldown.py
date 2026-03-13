class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        hold, sold, rest = [0] * n, [0] * n, [0] * n

        hold[0] = -prices[0]

        for i in range(n):
            # To be holding today - you must either
            # have been holding yesterday hold[i - 1]
            # or resting yesterday and bought today rest[i - 1] - prices[i]
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])

            # To be sold today - you must have been holding yesterday hold[i - 1]
            # and you sold today +prices[i]
            sold[i] = hold[i - 1] + prices[i]

            # To be in rest - you must either be in rest yesterday and did nothing
            # or sold state yesterday (so you're forced to rest today)
            rest[i] = max(rest[i - 1], sold[i - 1])

        return max(sold[n - 1], rest[n - 1])
