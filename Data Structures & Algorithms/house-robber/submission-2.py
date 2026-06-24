class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(len(nums)+1)
        dp[0] = nums[0]
        if n==1:
            return dp[n-1]
        dp[1] = max(nums[1], nums[0])
        if n<2:
            return nums[n-1]

        # max(cur + dp[i-2], dp[i-1]
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]