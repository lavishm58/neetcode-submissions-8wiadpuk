class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        vals = intervals
        vals.sort(key=lambda x:(x[0],x[1]))
        c = 0
        i=0
        while(i<len(vals)):
            cur_val = vals[i]
            i+=1
            while(i<len(vals) and vals[i][0]<cur_val[1]):
                cur_val[1] = min(cur_val[1], vals[i][1])
                c+=1                     
                i+=1
                        
        return c