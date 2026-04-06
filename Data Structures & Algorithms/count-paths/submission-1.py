class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(m-1,n-1)] = 1
        for i in range(n):
            dp[(m,i)] = 0
        for i in range(m):
            dp[(i,n)] = 0


        for i in range(m-1, -1,-1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1:
                    pass
                else:
                    dp[(i,j)] = dp[(i+1,j)] + dp[(i, j+1)]

        return dp[(0,0)]