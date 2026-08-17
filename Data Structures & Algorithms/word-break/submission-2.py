class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = dp[]

        # dp[2]= True, 0
        # st = 3 
        # dp[3] = subs(st, st+1) is word or dp[i-1] st to here is true 

        dp = {}
        dic = {}
        for word in wordDict:
            dic[word] = 1
        st = 0
        for i in range(len(s)):
            w = s[st:i+1]
            # print(w)
            if w in dic:
                dp[i] = st 
                st = i+1
            else:
                for j,k in dp.items():
                    if s[k:i+1] in dic or s[j+1:i+1] in dic:
                        dp[i] = k 
                        st = i+1
                        break 
        if len(s)-1 in dp:
            return True            
        return False 

