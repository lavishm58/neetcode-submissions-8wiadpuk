class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bn(ar, val):

            l = 0
            r = len(ar)-1
            # 2,3,4
            # l=0, r=3
            # m = 1
            # l=0, r=0

            while(l<=r):
                m = (l+r)//2
                if ar[m]==val:
                    return m
                if ar[m]<val:
                    l = m+1
                else:
                    r = m-1
            return -1

        for i, n in enumerate(numbers):
            val = target - n
            idx = bn(numbers[i+1:], val)


            if idx!=-1:
                return [i+1, idx+1 + (i+1)]
