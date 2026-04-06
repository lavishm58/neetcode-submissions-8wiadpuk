from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = defaultdict(list)
        for i in range(len(nums)):
            hash[nums[i]].append(i)

        ls = []
        dups = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if hash.get(-(nums[i] + nums[j]), None) is not None:
                    found = 0
                    for k in hash[-(nums[i] + nums[j])]:
                        if k not in [i,j]:
                            found = 1
                    print(found, nums[i], nums[j])
                    if found ==1:
                        triplets = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                        if dups.get('|'.join(str(triplets)), None) is None:
                            dups['|'.join(str(triplets))] = triplets
        final = []
        for dup in dups.values():
            final.append(dup)
        return final
