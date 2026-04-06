class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        n = len(h)
        mx_l = [0]*n
        mx_r = [0]*n
        mx = 0
        for i in range(n):
            mx = max(mx, h[i])
            mx_l[i] = mx 

        mx = 0
        for i in range(n-1,-1, -1):
            mx = max(mx, h[i])
            mx_r[i] = mx
        ar = 0

        for i in range(1,n-1):
            if mx_l[i-1]>0 and mx_r[i+1]>0 and min(mx_l[i], mx_r[i])>h[i]:
                ar+=min(mx_l[i], mx_r[i])-h[i]

        return ar
