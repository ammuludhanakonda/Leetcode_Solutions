class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            profit = prices[i] - min
            if profit > max_profit:
                max_profit = profit
        return max_profit