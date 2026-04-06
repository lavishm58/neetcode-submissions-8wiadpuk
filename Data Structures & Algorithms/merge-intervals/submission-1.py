class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:(x[0], x[1]))

        newvals = []
        vals = intervals
        i=0
        # [[1,2], [3,4], [3.5, 5]]
        while(i<len(vals)):
            
            curval = [vals[i][0], vals[i][1]]
            i+=1
            while(i<len(vals) and vals[i][0]<=curval[1]):
                curval[0] = min(curval[0], vals[i][0])
                curval[1] = max(curval[1], vals[i][1])
                i+=1
            newvals.append(curval)            
        return newvals