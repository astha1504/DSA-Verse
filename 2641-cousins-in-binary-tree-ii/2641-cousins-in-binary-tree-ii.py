class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque()
        q.append((root.val, root))
        root.val=0
        while q:
            n = len(q)
            level = 0
            for localsum, node in list(q):  
                if node.left:
                    level+=node.left.val
                if node.right:
                    level+=node.right.val
            for i in range(n):
                child = 0
                localsum,node=q.popleft()
                if node.left:
                    child+=node.left.val
                if node.right:
                    child+=node.right.val
                if node.left:
                    q.append((node.left.val, node.left))
                    node.left.val=level-child  
                if node.right:
                    q.append((node.right.val, node.right))
                    node.right.val=level-child  
        return root

        