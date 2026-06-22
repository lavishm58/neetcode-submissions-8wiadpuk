class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        h = heights
        max_ar = (r-l)*min(h[l], h[r])

        while l<r:
            max_ar = max(max_ar, (r-l)*min(h[l], h[r]))
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
        return max_ar

