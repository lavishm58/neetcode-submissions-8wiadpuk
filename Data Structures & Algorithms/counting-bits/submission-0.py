class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ls = []
        for i in range(0,n+1):
            c = 0
            while(i):
                i = i & (i-1)
                c+=1
            ls.append(c)
        return ls