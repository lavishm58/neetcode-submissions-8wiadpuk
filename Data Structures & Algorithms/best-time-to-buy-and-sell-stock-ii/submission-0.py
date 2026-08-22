class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b=prices[0]
        sm = 0
        for i in range(1,len(prices)):
            if prices[i]>b:
                sm+=(prices[i]-b)
            
            b = prices[i]
        return sm 
        