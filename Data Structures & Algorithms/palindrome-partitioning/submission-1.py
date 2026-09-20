class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = []
        res = []
        st=0
        i=0
        if s=='':
            return [[]]
        def is_palin(s):
            i=0
            j=len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False 
            return True
        def dfs(st, i, subset, cut):
            # print(st, i, subset, cut, len(s))
            if i>=len(s):
                if cut:
                    res.append(subset.copy())
                return 
        
            if is_palin(s[st:i+1]):
                subset.append(s[st:i+1])
                dfs(i+1,i+1, subset, True)
                subset.pop()
                if i+1<len(s):
                    dfs(st, i+1, subset, False)
            else:
                if i+1<len(s):
                    dfs(st, i+1, subset, False)
        dfs(st,i, subset, True)

        return res 