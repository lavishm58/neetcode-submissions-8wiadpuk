class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums)-1
        req = 0
        while(i>=0):
            if nums[i]>=req:
                if i==0:
                    return True
                req=1
            else:
                req+=1                
            i-=1
        return False