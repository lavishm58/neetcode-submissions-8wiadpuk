import string
from collections import defaultdict
class Solution:
    def check(self, s):
        mx = 0
        d = defaultdict(int)
        for ch in s:
            d[ch]+=1
        ch = None
        for k, v in d.items():
            if v>mx:
                mx = v
                ch = k
        # print(d, ch, mx)
        if ch:
            del d[ch]
        # print(d, 'check')
        return sum(d.values())
    def characterReplacement(self, s: str, k: int) -> int:
        st = 0
        i=0
        n = len(s)
        dic = defaultdict(int)
        mx = 0
        while(st<n and i<n):
            # print(st,i, n, self.check(s[st:i]))
            if self.check(s[st:i+1])<=k:
                mx = max(mx, i-st+1)                    
            else:
                st+=1
                # if k==0:
                #     st+=2
            i+=1
        return mx