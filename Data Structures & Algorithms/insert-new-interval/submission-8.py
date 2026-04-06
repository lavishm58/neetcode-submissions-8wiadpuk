class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval[0], newInterval[1]
        i=0
        vals = intervals
        newvals = []
        if vals==[]:
            vals.append([a,b])
            return vals
        while i< len(vals) and vals[i][1]<a:
            newvals.append(vals[i])
            i+=1
        
        newval = [a,b]
        while i<len(vals) and newval[1]>=vals[i][0]:
            # print(a, vals[i][0],'dsvf')
            newval[0] = min(newval[0], vals[i][0])
            newval[1] = max(newval[1], vals[i][1])
            i+=1
        newvals.append(newval)

        while i<len(vals):
            newvals.append(vals[i])
            i+=1
        return newvals 
