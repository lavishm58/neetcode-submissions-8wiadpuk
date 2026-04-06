class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pats, atls = set(), set()
        def dfs(r,c, heights, visited, prev):
            if (r,c) in visited or r<0 or c<0 or r>=ROWS or c>=COLS or \
                heights[r][c]<prev:
                return
            visited.add((r,c))
            dfs(r+1,c, heights, visited, heights[r][c])
            dfs(r,c+1, heights, visited, heights[r][c])
            dfs(r-1,c, heights, visited, heights[r][c])
            dfs(r,c-1, heights, visited, heights[r][c])
        
        for r in  range(ROWS):
            dfs(r,0, heights, pats, heights[r][0])
            dfs(r,COLS-1, heights, atls, heights[r][COLS-1])
        for c in  range(COLS):
            dfs(0,c, heights, pats, heights[0][c])
            dfs(ROWS-1,c, heights, atls, heights[ROWS-1][c])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pats and (r,c) in atls:
                    res.append((r,c))
        return res