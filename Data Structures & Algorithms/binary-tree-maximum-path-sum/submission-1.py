# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ar = []
        v = 0
        self.dic = {}
        self.res = root.val
        def dfs(root):
            if not root:
                return 0

            
            lmax = max(dfs(root.left), 0)
            rmax = max(dfs(root.right), 0)
            # lmax = max(0, lmax)
            # rmax = max(0, rmax)
            val = lmax + root.val + rmax
            self.res = max(self.res, val)
            # print('csjdchbsd')

            return root.val + max(lmax, rmax)

        dfs(root)
        # print(self.dic)
        return self.res