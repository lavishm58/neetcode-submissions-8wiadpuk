# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def invert(root):
            left = root.left
            right = root.right
            root.left = right
            if root.left:
                invert(root.left)
            root.right = left
            if root.right:
                invert(root.right)
            return root
        if not root:
            return root
        return invert(root)

        