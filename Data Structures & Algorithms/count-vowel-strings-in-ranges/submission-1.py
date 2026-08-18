class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            l,r = q
            c=0
            for i in range(l,r+1):
                if words[i][0] in ['a', 'e', 'i', 'o','u'] and \
                    words[i][-1] in ['a', 'e', 'i', 'o','u']:
                    c+=1
            ans.append(c)
        return ans 
