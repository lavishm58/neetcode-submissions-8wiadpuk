# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def issame(p, q):
            if (not p and q) or (p and not q):
                return False
            if (not p and not q):
                return True

            if p.val!=q.val:
                return False

            return issame(p.left, q.left) and issame(p.right, q.right)
        
        q = deque()
        q.append(root)

        check = False
        while(q):
            n = q.popleft()
            # print(n.val, subRoot.val, 'dfvf')
            if n.val == subRoot.val:
                # print(' sjdvhbdf ')
                check = issame(n, subRoot)
                if check:
                    return check
            if n.left:
                q.append(n.left)

            if n.right:
                q.append(n.right)

        return check
