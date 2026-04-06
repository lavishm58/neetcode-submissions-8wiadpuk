class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global visited
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def mark(grid, visited, i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 
            if grid[i][j]=="1" and not visited[i][j]:
                visited[i][j] = True
            else:
                return
            mark(grid, visited, i, j+1)
            mark(grid, visited, i+1, j)
            mark(grid, visited, i, j-1)
            mark(grid, visited, i-1, j)
            return 
        c = 0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    mark(grid, visited, i, j)
                    c+=1
        return c
