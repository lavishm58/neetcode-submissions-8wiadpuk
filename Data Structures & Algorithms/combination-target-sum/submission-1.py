class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset):
            cur_sum = sum(subset)
            # print(subset, cur_sum)
            if cur_sum==target:
                res.append(subset.copy())
                return 
            elif cur_sum>target or i>=len(nums):
                return 
            subset.append(nums[i])
            dfs(i,subset)        
            subset.pop()
            dfs(i+1, subset)
            return 

        dfs(0, [])
        return res 

