class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        mxst = None
        mxln = 0
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                
                if s[i]==s[j] and ((j-i)<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    # print('mxln', mxln, mxst, j, i)
                    if j-i+1>mxln:
                        mxln = j-i+1
                        mxst = i
                        
        return s[mxst:mxst+mxln]