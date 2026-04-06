class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = 1e9
            for c in coins:

                if amount-c>=0:
                    res = min(res, 1+ dfs(amount-c))
            dp[amount] = res
            return res
        
        res = dfs(amount)
        return -1 if res>=1e9 else res