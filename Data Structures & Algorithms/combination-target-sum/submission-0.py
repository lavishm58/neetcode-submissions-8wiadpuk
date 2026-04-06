class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ar = []
        dic = {}
        def comb(i, target, ar, nums):
            if sum(ar)>target:
                return
            if sum(ar)==target:
                dic['-'.join([str(v) for v in ar]) ] = 1
            
            if i>=len(nums):
                return

            comb(i, target, ar + [nums[i]], nums)
            comb(i+1, target, ar, nums)
            # comb(i, target, ar, nums)
        comb(0, target, ar, nums)
        ars = []
        for k, _ in dic.items():
            # print()
            ars.append([int(v) for v in k.split('-')])
        return ars