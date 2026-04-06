# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        l = 0
        if not root:
            return []
        q.append([root, 0])
        dic = defaultdict(list)
        
       
        while(q):
            
            n,l = q.popleft()
            
            dic[l].append(n.val)
            if n.left:
                q.append([n.left, l+1])
                
            if n.right:
                q.append([n.right, l+1])
        ar = []
        for k, v in dic.items():
            ar.append(v)
        return ar