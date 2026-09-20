class Solution:
    def longestPalindrome(self, s: str) -> str:
      dp = [[False]*(len(s)+1) for _ in range(len(s)+1)]
      mx = 0 
      mx_str = ''
      for i in range(len(s)-1,-1,-1):
        for j in range(i, len(s)):
          if s[i]==s[j] and (dp[i+1][j-1] or j-i+1<=2):
            dp[i][j] = True 
            if j-i+1>mx:
              mx = j-i+1
              mx_str = s[i:j+1]
      return mx_str