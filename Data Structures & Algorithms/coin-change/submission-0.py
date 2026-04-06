class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        minln = None

        dp = {}
        # for c in coins:
        #     dp[c] = 1

        def dfs(target):
            if target ==0:
                return 0
            elif target in dp:
                return dp[target]

            res = 1e9
            
            for c in coins:
                if target-c>=0:
                    res = min(res, 1+dfs(target-c))
            dp[target] = res            
            return res

        ans = dfs(amount)

        print(dp)
        return -1 if ans>=1e9 else ans