class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        # 5 6 1 2 3 4
        # 5 1 2 3 4
        # 3 4 5 6 1 2 
        # 1 2 3 4  

        # 4 5 1 2 3

        res = nums[0]
        while(l<=r):

            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
                break

            if nums[mid]<nums[r]:
                r = mid-1
            else:
                l = mid+1

        return res

