class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        collect = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    collect.append((i,j))
        
        for x,y in collect:
            for i in range(len(matrix)):
                matrix[i][y] = 0
            for i in range(len(matrix[0])):
                matrix[x][i] = 0

        return None