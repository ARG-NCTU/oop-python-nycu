# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 基底情況：葉子節點
        if not root.left and not root.right:
            return root.val == 1
        
        # 遞迴評估左右子節點
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # 根據節點值應用布林運算
        if root.val == 2:
            return left_val or right_val
        return left_val and right_val