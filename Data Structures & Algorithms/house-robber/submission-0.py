class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [None for _ in range(len(nums))]
        def take(i):
            if i<0:
                return 0
            if dp[i]:
                return dp[i]

            dp[i] = max(nums[i] + take(i-2), take(i-1))
            return dp[i]
        
        return take(len(nums)-1)
