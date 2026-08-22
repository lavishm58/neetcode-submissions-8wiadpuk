class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ar = []
        for i in range(len(matrix)):
            ar.extend(matrix[i])
        l=0
        r = len(ar)-1
        while l<=r:
            m = (l+r)//2
            if ar[m]==target:
                return True 
            if ar[m]<target: 
                l=m+1 
            else:
                r=m-1 
        return False 
        