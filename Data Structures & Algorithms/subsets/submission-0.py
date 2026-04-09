import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ar = []
        # 1 2 3
        # i=0, j=0
        def comb(nums, i, cur, ar):

            if i==len(nums):
                ar.append(cur.copy())
                return ar          
            cur.append(nums[i])            
            comb(nums, i+1, cur, ar)
            cur.pop()
            comb(nums, i+1, cur, ar)
            return ar
        ar = comb(nums, 0, [], ar)
        # for i in range(len(nums)):
        #     # 1,1
        #     for j in range(i+1, len(nums)+1):
        #         ar.append(nums[i:j])
        return ar