class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > max:
                max = prices[i] - buy
        if max > 0:
            return max
        else:
            return 0
