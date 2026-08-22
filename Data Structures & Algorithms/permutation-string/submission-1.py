class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for i in range(len(s1)):
            dic[s1[i]]=1 + dic.get(s1[i], 0)

        for i in range(len(s2)):
            if s2[i] in dic:
                newdic = {}
                for j in range(i,min(i+len(s1), len(s2))):
                    if s2[j] in dic:
                        newdic[s2[j]] = 1+newdic.get(s2[j],0)

                if newdic==dic:
                    return True 
        
        return False 
