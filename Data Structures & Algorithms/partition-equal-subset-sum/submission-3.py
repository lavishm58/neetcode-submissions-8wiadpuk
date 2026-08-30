from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = defaultdict(bool)
        next_dp  = defaultdict(bool)

        dp[0]=True 

        for n in nums:
            for t in range(1,target+1):
            
                if t-n>=0:
                    next_dp[t] = dp[t] or dp[t-n]
                else:
                    next_dp[t] = dp[t]
            next_dp, dp = dp, next_dp 

        return dp[target]



