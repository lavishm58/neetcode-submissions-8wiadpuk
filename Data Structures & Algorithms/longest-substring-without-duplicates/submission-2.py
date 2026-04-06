class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        a = 0
        cur = 0
        mx = 0
        n = len(s)
        while(cur<n):
            if dic.get(s[cur],-1)<a:
                dic[s[cur]] = cur
                mx = max(mx, cur-a+1)
                # print(a, cur, dic)
                cur+=1
            else:
                a = dic[s[cur]]+1
                dic[s[cur]] = cur
                cur+=1
        return mx
