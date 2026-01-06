# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        lvl, ans, mx = 1, 1, float('-inf')
        while q:
            s = 0
            for _ in range(len(q)):
                n = q.popleft()
                s += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            if s > mx:
                mx, ans = s, lvl
            lvl += 1
        return ans

        