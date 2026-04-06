class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights)-1
        max_ar = 0
        h = heights
        while(a>=0 and a<b and b>0):
            max_ar = max(max_ar, (b-a)*min(h[a], h[b]))
            if h[a]>=h[b]:
                b-=1
            else:
                a+=1
        return max_ar