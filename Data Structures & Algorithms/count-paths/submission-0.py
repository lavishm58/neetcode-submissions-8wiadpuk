class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif i<0 or i>m-1 or \
                j<0 or j>n-1:
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            
            ans = dfs(i+1,j) + dfs(i, j+1)
            dp[(i,j)] = ans
            return ans

        return dfs(0,0)