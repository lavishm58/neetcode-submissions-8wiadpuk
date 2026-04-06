class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp1 = [None for _ in range(len(nums))]
        dp2 = [None for _ in range(len(nums))]
        
        def take(i, nums, dp):
            # print(i, nums)
            if i<0:
                return 0
            elif dp[i]:
                return dp[i]
            # print(i)            
            dp[i] = max(nums[i]+ take(i-2, nums, dp), take(i-1, nums, dp))
            return dp[i]
        
        n = len(nums)
        if n==1:
            return nums[0]
        # take(n-2, nums[1:n])
        # print('dp', dp)
        # return 0
        # return 

        return max(take(n-2, nums[0:n-1], dp1),take(n-2, nums[1:n], dp2))
