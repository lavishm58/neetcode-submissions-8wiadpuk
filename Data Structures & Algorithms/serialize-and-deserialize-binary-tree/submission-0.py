# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        q = deque()
        q.append([root, 1])
        ar = []
        d = depth(root)
        print('depth ', d)
        while(q):
            n, cur = q.popleft()
            if n:
                ar.append(n.val)
            else:
                ar.append(None)

            if n and n.left:
                q.append([n.left, cur+1])
            else:
                if cur+1<=d:
                    q.append([None, cur+1])
            if n and n.right:
                q.append([n.right, cur+1])
            else:
                if cur+1<=d:
                    q.append([None, cur+1])
        ar= [str(v) for v in ar]
        print('ar ', ar)
        return '-'.join(ar)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ar = data.split('-')

        for i, v in enumerate(ar):
            if v=='None':
                ar[i] = None
            else:
                ar[i] = int(v)

        def left(i):
            return 2*i+1
        def right(i):
            return 2*i+2
        # print('acv r', ar)
        def build(i, ar):
            if i>len(ar)-1 or ar[i] is None:
                return None
            root = TreeNode(ar[i])
            root.left = build(left(i), ar)
            root.right = build(right(i), ar)
            return root

        return build(0, ar)
