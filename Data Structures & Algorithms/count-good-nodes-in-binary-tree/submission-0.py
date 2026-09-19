# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [(root, -1e9)]
        count = 0
        while q:
            node, max_val = q.pop()
            if node.val>=max_val:
                count+=1
            if node.left is not None:
                q.append((node.left, max(node.val, max_val)))
            if node.right is not None:
                q.append((node.right, max(node.val, max_val)))
        return count 
