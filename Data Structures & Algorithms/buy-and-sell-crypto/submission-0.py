class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        buy = prices[l]
        for r in range(1, len(prices)):
            sell = prices[r]
            if buy > sell:
                l = r
                buy = prices[l]
            profit = max(profit, sell - buy)

        return profit            
        