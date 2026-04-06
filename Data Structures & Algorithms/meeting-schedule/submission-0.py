"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        vals = []
        for val in intervals:
            vals.append([val.start, val.end])
        vals.sort(key=lambda x:(x[0], x[1]))
        
        i=0

        while(i<len(vals)):
            curval = [vals[i][0], vals[i][1]]
            i+=1
            while(i<len(vals) and vals[i][0]<curval[1]):
                return False

        return True