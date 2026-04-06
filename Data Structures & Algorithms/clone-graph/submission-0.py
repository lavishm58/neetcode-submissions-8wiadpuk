"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        q.append(node)
        ls = []
        oldtonew = {node:Node(node.val)}        
        while(q):
            n = q.popleft()
            nbs = n.neighbors
            for nb in nbs:
                if nb not in oldtonew:
                    oldtonew[nb] = Node(nb.val) 
                    q.append(nb)
                oldtonew[n].neighbors.append(oldtonew[nb])

        return oldtonew[node] if node else None
