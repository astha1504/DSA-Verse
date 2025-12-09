# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr=0
        def dfs(node):
            nonlocal curr
            if not node:
                return 0
            if low<=node.val<=high:
                curr+=node.val
            if node.val>low:
                dfs(node.left)
            if node.val<high:
                dfs(node.right)
        dfs(root)
        return curr        