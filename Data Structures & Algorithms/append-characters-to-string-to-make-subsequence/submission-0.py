class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i, ch in enumerate(s):
            if ch == t[j]:
                j+=1
            if j==len(t):
                break 
        return len(t)-j 
