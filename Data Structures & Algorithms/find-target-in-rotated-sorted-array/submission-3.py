class Solution:
    def bs(self, l, r, a, target):
        # l = 0
        # r = len(a)-1
        t = target
        while(l<=r):
            m = (l+r)//2
            print(m, l, r,a[m], target, 'erg')
            if a[m]==t:
                return m
            if t>a[m]:
                l = m+1
            else:
                r = m-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1   
        res = nums[0]
        a = nums
        dic = {}
        while(l<=r):        
            if a[l]<=a[r]:
                res = min(res, a[l])
                dic[a[l]] = l

            m = (l+r)//2
            if a[m]<=a[l] and a[m]<=a[r]:
                res = min(res, a[m])
                dic[a[m]] = m

            if a[l]<=a[m]:
                l = m+1
            else:
                r = m-1
        idx = dic.get(res, -1)
        val = -1
        if idx!=-1:
            val = self.bs(idx, len(a)-1, a, target)
            if val==-1:
                val = self.bs(0, idx-1, a, target)
        else:
            val = self.bs(0, len(a)-1, a, target)
        return val




        
