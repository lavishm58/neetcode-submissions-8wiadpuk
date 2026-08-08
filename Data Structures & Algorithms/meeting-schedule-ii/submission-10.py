"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        vals = intervals
        st = [val.start for val in vals]
        end = [val.end for val in vals]
        st.sort()
        end.sort()
        c = 0
        mx = 0
        print(st)
        print(end)
        s = e = 0

        while s<len(vals):
            if st[s]<end[e]:
                s+=1
                c+=1 
            else:
                e+=1
                c-=1
            mx = max(mx, c)
        return mx

# m1 0-10 10-20 20-30 30-40
# m2 0-100
# m3 10-90
# m4 20-80