# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ar = []

        def smallestk(root,k, ar):
            
            if not root:
                return None

            # if k == len(ar):
            #     return ar[-1]
            
            smallestk(root.left, k, ar)                        
            ar.append(root.val)
            smallestk(root.right, k, ar)

        smallestk(root,k, ar)

        return ar[k-1]

