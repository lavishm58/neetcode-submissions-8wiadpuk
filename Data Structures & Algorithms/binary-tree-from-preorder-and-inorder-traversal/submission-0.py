# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h = {v:i for i, v in enumerate(inorder)}

        self.i = 0
        def build(l, r):
            if l>r:
                return None
           
            root_val = preorder[self.i]
            m = h[root_val]
            self.i+=1
            root = TreeNode(root_val)
            
            root.left = build(l, m-1)
            root.right = build(m+1, r)

            return root

        return build(0, len(preorder)-1)
