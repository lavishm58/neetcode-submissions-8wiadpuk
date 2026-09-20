class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1,2,3

        # 2,3

        # if len(nums)==0:
        #     return [[]]
        # permutes = self.permute(nums[1:])
        # res = []
        # for p in permutes:
        #     for i in range(len(p)+1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)

        permutes = [[]]
        res = []
        for n in nums:
            new_permute = []
            for p in permutes:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_permute.append(p_copy)
            permutes = new_permute                   
                    # res.append(p_copy)
        # print(permutes)
        return permutes         
