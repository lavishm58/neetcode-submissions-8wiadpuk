class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for p in points:
            temp = [p, p[0]**2 + p[1]**2]
            ans.append(temp)
        ans = sorted(ans, key=lambda x:x[1])[0:k]
        return [a[0] for a in ans]