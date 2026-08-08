import heapq

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        dic = defaultdict(int)
        for n in nums:
            dic[n]+=1
        max_heap = []
        for a, b in dic.items():
            heapq.heappush(max_heap, [-b,a])
        els = []
        for i in range(k):
            val = heapq.heappop(max_heap)
            els.append(val[1])
        return els