class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i]<=b:
                b = min(b, prices[i])
            else:
                profit = max(profit, prices[i]-b)
        return profit
