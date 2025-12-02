from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])  
        count = 0       
        while q:
            node = q.popleft()  
            count += 1     
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return count
