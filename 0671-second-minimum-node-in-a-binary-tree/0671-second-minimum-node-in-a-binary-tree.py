# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        val=root.val
        self.second=float('inf')
        def dfs(node):
            if not node:
                return
            if val<node.val<self.second:
                self.second=node.val
            elif node.val==val:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        if self.second<float('inf'):
            return self.second
        else:
            return -1    