# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return []
            l = dfs(node.left)
            r = dfs(node.right)
            return l + [node.val] + r
        
        arr = dfs(root) 
        def build(arr, lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(arr[mid])
            node.left = build(arr, lo, mid - 1)
            node.right = build(arr, mid + 1, hi)
            return node
        
        return build(arr, 0, len(arr) - 1)
