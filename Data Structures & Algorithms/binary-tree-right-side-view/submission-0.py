# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layers = defaultdict(list)
        if root is None:
            return []
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            layers[level].append(node.val)
            if node.left is not None:
                q.append((node.left, level+1))
            if node.right is not None:
                q.append((node.right, level+1))
        ans = []
        for i in range(len(layers)):
            ans.append(layers[i][-1])
        return ans 
        
