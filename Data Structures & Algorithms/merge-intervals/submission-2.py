class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:(x[0], x[1]))
        vals = intervals
        new_val = []
        i=0
        res=  []
        while(i<len(vals)):
            cur_val = vals[i]

            i = i+1
            while i<len(vals) and intervals[i][0]<=cur_val[1]:
                cur_val = [min(cur_val[0], intervals[i][0]), max(cur_val[1], intervals[i][1])]
                i+=1            
            res.append(cur_val)
        return res