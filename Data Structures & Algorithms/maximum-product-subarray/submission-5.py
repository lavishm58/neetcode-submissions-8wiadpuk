class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totmax = nums[0]
        curMin,curMax = 1,1
        for i in range(len(nums)):            
            tmp = curMax*nums[i]
            curMax = max(curMax*nums[i], curMin*nums[i], nums[i])                
            curMin = min(curMin*nums[i], nums[i], tmp)
            totmax = max(totmax, curMax)



        return totmax