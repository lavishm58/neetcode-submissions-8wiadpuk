from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = {}

        def dfs(v):
            # print(v, 'erg', v in visited)
            # if v in visited:
            #     return False
            visited[v] = True

            for a in adj[v]:
                if a not in visited and not dfs(a):
                    return False
            return True
        c = 0
        for v in range(n):
            if v not in visited:
                # print(v)
                dfs(v)
                c+=1
            if len(visited)==n:
                break
        
        return c

