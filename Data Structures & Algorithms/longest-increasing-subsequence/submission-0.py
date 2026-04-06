class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        mx = 0
        curar = []
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        def dfs(i, j):
            if i>=len(nums):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            LIS = dfs(i+1, j)

            if j==-1 or nums[j]<nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i))
            
            dp[i][j] = LIS

            return LIS

        

        return dfs(0, -1)
