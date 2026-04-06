class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class MedianFinder:

    def __init__(self):
        self.root = None

    def addNum(self, num: int) -> None:


        def add(root, num):
            if not self.root:
                self.root = TreeNode(num)
                return        
            if num>root.val and not root.right:
                root.right = TreeNode(num)
                return
            elif num>root.val and root.right:
                add(root.right, num)
            elif num<=root.val and not root.left:
                root.left = TreeNode(num)
                return
            elif num<=root.val and root.left:
                add(root.left, num)
        add(self.root, num)
    
    def get_ar(self):
        self.ar = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.ar.append(root.val)
            dfs(root.right)
        dfs(self.root)
        return self.ar

    def findMedian(self) -> float:
        self.ar = self.get_ar()
        # print(self.ar, self.root.val)
        if len(self.ar)%2==0:
            x = len(self.ar)//2
            # print(x, self.ar)
            return (self.ar[x]+self.ar[x-1])/2
        else:
            return self.ar[len(self.ar)//2]

