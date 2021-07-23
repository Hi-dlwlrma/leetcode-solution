class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        a = prices[0]
        
        for i in range(len(prices)):
            b = prices[i]
            if a > b:
                a = b
            elif a < b:
                profit = b - a
                if i+1 < len(prices) and b > prices[i+1]: # condition to buy that stock, b = peak
                    max_profit = max_profit + profit
                    a = prices[i+1] # sold out, so set up a
                elif i+1 == len(prices):
                    max_profit = max_profit + profit
                    
        return max_profit
