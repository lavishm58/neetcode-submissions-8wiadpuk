class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # crats crabt
  
        # i,j = 3, 4 = 1

        # 2,2 = 3,2 2,3 3,3 (1)

        # 3,2 = 3,3, 4,3 4,2
        # 3,3 = 1
        if text1=='' or text2=='':
            return 0

        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        # print(dp)
        # print(len(dp), len(dp[0]))
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1, -1, -1):
                # crabt
                # cat
                if text1[i]==text2[j]:
                    # print(i, j)
                    # print(dp, 'dfv')
                    mx = 1
                    # if i+1<len(text1):
                    #     mx = max(mx, 1+dp[i+1][j])
                    if i+1<len(text1) and j+1<len(text2):
                        mx = max(mx, 1+dp[i+1][j+1])
                    # if j+1<len(text2):
                    #     mx = max(mx, 1+dp[i][j+1])
                    
                else:
                    mx = max(max(dp[i][j+1], dp[i+1][j]), dp[i+1][j+1])
                dp[i][j] = mx
        # print(dp)
        # i,j = i+1,j  i+1, j+1, i,j+1
        return dp[0][0]