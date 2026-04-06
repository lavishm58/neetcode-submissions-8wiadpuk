class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices
        n= len(p)
        if n<=1:
            return 0
        pr = 0
        mx_r = [0]*n
        mx = 0
        for i in range(n-1,-1,-1):
            mx = max(mx, p[i])
            mx_r[i] = mx
        
        for i in range(n-1):
            if p[i]<mx_r[i+1]:
                pr = max(pr, mx_r[i+1]-p[i])
        return pr