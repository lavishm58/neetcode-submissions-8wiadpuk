class Solution:
    def findMin(self, nums: List[int]) -> int:
        #  4 5 6 1 2 3

        def bs(l, r, ar):
            res = ar[0]
            while l<=r:
                print(l, r)
                if ar[l]<ar[r]:

                    res = min(res, ar[l])
                    break
                m = (l+r)//2
                res = min(res, ar[m])
                if ar[l]>ar[m]:
                    r = m-1
                else:
                    l = m+1

            return res

        return bs(0, len(nums)-1, nums)
