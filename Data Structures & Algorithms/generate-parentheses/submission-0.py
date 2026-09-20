class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_c = 0
        close_c = 0
        i = 0
        res = []
        subset = ''
        def dfs(i, open_c, close_c, subset):
            if i==n:
                subset_copy = subset
                res.append(subset)
            
            if open_c+1<=n:
                # print(subset, open_c,close_c, n)
                subset += '('
                dfs(i, open_c+1, close_c, subset)
                subset = subset[:-1]
            if close_c+1<=n and close_c+1<=open_c:
                subset+=')'
                dfs(i+1, open_c, close_c+1, subset)
        dfs(i, open_c, close_c, subset)
        return res 
