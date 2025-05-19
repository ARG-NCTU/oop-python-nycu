from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0 or root.val == 1:
            return bool(root.val)
        result = (self.evaluateTree(root.left), self.evaluateTree(root.right))
        return any(result) if root.val == 2 else all(result) 