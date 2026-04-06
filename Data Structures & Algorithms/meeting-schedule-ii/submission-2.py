"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        vals = []

        for val in intervals:
            vals.append([val.start, val.end])
        vals.sort(key = lambda x:(x[0], x[1]))
        if vals == []:
            return 0
        i = 0
        mx = 1
        # [(0,40),(5,10),(15,20)]
        # print(vals, 'sorted')
        max_time = None
        while(i<len(vals)):
            
            curval = [vals[i][0], vals[i][1]]

            i+=1
            if max_time is not None and max_time>curval[1]:
                pass
            else:
                c = 1
            while(i<len(vals) and vals[i][0]<curval[1]):
                curval[0] = max(curval[0], vals[i][0])
                curval[1] = min(curval[1], vals[i][1])
                max_time = max(curval[1], vals[i][1])
                i+=1
                c+=1
                mx = max(mx, c)
        return mx