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
        vals.sort(key = lambda x:x[0])
        if vals == []:
            return 0
        heap = []
        for val in vals:
            if heap and val[0]>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, val[1])
        return len(heap)

# m1 0-10 10-20 20-30 30-40
# m2 0-100
# m3 10-90
# m4 20-80