class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # -1, 3,-4,2
        
        # -2, 
        # dp = {}
        mx = int(-1e9)
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            mx = max(mx, sm)
            if sm<0:
                sm = 0
            
                
        # print(mx)
        return mx        