class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        n = len(s)
        st = 0
        ln = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (s[i]==s[j] and (j-i)<=2) or (s[i]==s[j] and dp[i+1][j-1]):       
                    dp[i][j] = True
                    if (j-i+1)>ln:
                        st = i
                        ln = (j-i+1)
        
        return s[st:st+ln]
