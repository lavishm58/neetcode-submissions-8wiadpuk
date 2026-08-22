class Solution:
    def numSquares(self, n: int) -> int:
        # 1,4,9


        # 1,4
        dp = [n]*(n+1)
        dp[1] = 1
        dp[0]=0
        for target in range(1,n+1):
            
            for s in range(1,target+1):
                sq = s*s
                if sq>n:
                    break 
                dp[target] = min(dp[target], 1+dp[target-sq])
        return dp[target]
