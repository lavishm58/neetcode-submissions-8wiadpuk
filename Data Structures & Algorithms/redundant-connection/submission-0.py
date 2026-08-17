# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         # check if everyone has 2 edges then remove last one
#         # remove greater than 1 and check
#         1 - [2,3,4]
#         2 - [1]
#         3 - [1,4]
#         4 - [1,3]
#         5 - [4]
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        visited = defaultdict(bool)
        def dfs(u, par):
            if visited[u]:
                return True 

            visited[u] = True             
            for n in adj[u]:
                if n==par:
                    continue
                if dfs(n, u):
                    return True 
            return False 

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if dfs(u, -1):
                return [u,v]
            visited = defaultdict(bool)
        return edges[0]

