class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        vals = intervals
        vals.sort(key=lambda x:(x[0],x[1]))

        c = 0
        i=0
        # [[1,2],[1.5,3], [2,4]]
        # [[1,2],[1.5,2], [2,3]]
        newvals = []
        print(vals, 'sorted')
        while(i<len(vals)):
            curval = [vals[i][0], vals[i][1]]
            i+=1
            if i<len(vals):
                print(curval, vals[i])
            # 6
            while(i<len(vals) and vals[i][0]<curval[1]):
                # if 
                # curval[0] = min(curval[0], vals[i][0])
                curval[1] = min(curval[1], vals[i][1])
                i+=1
                c+=1
                        
        return c