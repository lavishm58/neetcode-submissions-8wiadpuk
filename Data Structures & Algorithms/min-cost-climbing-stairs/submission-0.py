class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)

        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])

# 0,1,2,3

        for i in range(0,n+1):
            if i==n:
                dp[i] = min(dp[i-1], dp[i-2])
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # print(dp)
        return dp[n]


        # [1,2,3,4,8,3,4,8]