class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp


        # 1 2 3 4 5
        n = len(nums)
        dp1 = [0]*n
        dp2 = [0]*n
        # dp[5] = 5th + dp[i-2], dp[4]
        # 1,3,5

        dp1[0] = nums[0]
        dp2[0] = 0
        if n==1:
            return nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]
        if n==2:
            return dp1[1]
        # dp1[2] = max(nums[2]+dp1[0], dp1[1])
        # dp2[2] = max(nums[2], nums[1])        
        # if n==3:
        #     return max(dp1[2], dp2[2])

        for i in range(2,len(nums)):
            if i==n-1:
                dp1[i] = dp1[i-1]
            else:
                dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])

            dp2[i] =  max(nums[i] + dp2[i-2], dp2[i-1])

        return max(dp1[n-1], dp2[n-1])