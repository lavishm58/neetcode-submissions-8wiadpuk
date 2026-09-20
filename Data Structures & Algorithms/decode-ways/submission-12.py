class Solution:
    def numDecodings(self, s: str) -> int:
        # 123205

        # if s[i-1:i+1]<26 and >0:
        #     dp[i-2]
        # if s[i]>0:
        #     dp[i-1]

        # dp[1] = 2
        if s=='':
            return 0
        dp = [0]*(len(s)+1)
        dp[0]=1
        if int(s[0])>0:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            if int(s[i-2:i])<27 and int(s[i-2:i])>0 and s[i-2]!='0':
                dp[i]+=dp[i-2]
                # print('dvfdfv',i, dp)
            if int(s[i-1])>0:
                dp[i]+=dp[i-1]
                # print('dvv',i, dp)
        return dp[len(s)]
