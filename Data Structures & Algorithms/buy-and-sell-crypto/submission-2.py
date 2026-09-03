class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                profit = max(profit, diff)
            right += 1
        return profit
