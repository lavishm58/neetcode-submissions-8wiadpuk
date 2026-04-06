class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [None for _ in range(n+1)]
        def climb(n):
            if n==0:
                return 1
            elif n<0:
                return 0
            elif dp[n]:
                return dp[n]

            dp[n] = climb(n-1) + climb(n-2)
            return dp[n]
        
        return climb(n)

            