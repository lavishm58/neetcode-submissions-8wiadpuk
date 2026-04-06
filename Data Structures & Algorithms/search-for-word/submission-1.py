class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()

        def comb(i, j, k):
            if k==len(word):
                return True
            if i>=len(board) or j>=len(board[0]) or i<0 or j<0 or (i,j) in path or \
                word[k]!=board[i][j]:
                return False
            path.add((i,j))
            res = comb(i+1,j,k+1) or \
                    comb(i-1,j,k+1) or \
                    comb(i,j+1,k+1) or \
                    comb(i,j-1,k+1)
            path.remove((i,j))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if comb(r,c,0):
                    return True
        return False
        
            # else:
            #     comb(i+1,j,'')
            #     comb(i,j+1,'')
            #     return

        comb(0, 0, '')

        if len(dic)>0:
            return True
        return False
