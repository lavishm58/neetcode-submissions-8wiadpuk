class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [5,6,7,1,2,3,4]

        l= 0
        n = len(nums)-1
        r = n
        # [3,4,4,5,6,1,2,2]
        while(l<=r):
            m = (l+r)//2
            #print(m, nums[m])
            if nums[m]==target:
                return True
            
            if nums[l]<nums[m]: 
                # t = 4
                if target<nums[m] and target>=nums[l]:
                    r = m-1 
                # t = 2
                else:
                    l = m+1
            elif nums[m]<nums[l]: 
                # t = 4
                if target<=nums[r] and target>nums[m]:
                    l = m+1 
                # t = 2
                else:
                    r = m-1
            else:
                l+=1

        return False 

        