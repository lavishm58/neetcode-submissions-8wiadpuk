class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        x,y = 0,0
        ls = []
        n = len(matrix)


        l,r,t,b = 0, len(matrix[0]), 0, n
        print(l,r,t,b)
        while(l<r and t<b):

            for i in range(l, r):
                ls.append(matrix[t][i])
            t+=1

            for i in range(t, b):
                ls.append(matrix[i][r-1])
            r-=1
            if not (l<r and t<b):
                break
                 
            for i in range(r-1,l-1, -1):
                ls.append(matrix[b-1][i])
            b-=1

            for i in range(b-1,t-1, -1):
                ls.append(matrix[i][l])
            l+=1
        return ls

