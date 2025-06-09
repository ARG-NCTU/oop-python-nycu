from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Evaluate a full binary tree representing boolean expressions and return the result.

        A full binary tree consists of nodes with values representing boolean operations and leaf nodes representing boolean values.
        For non-leaf nodes:
            - Value 2 represents boolean OR operation.
            - Value 3 represents boolean AND operation.
        For leaf nodes:
            - Value 0 represents False.
            - Value 1 represents True.

        Parameters:
            root (Optional[TreeNode]): The root of the full binary tree.

        Returns:
            bool: The boolean result of evaluating the root node.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> root1 = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
            >>> solution.evaluateTree(root1)
            True

            # Example 2:
            >>> root2 = TreeNode(0)
            >>> solution.evaluateTree(root2)
            False
        """
        if root.val == 0 or root.val == 1:
            return bool(root.val)

        result = (self.evaluateTree(root.left), self.evaluateTree(root.right))
        return any(result) if root.val == 2 else all(result) 
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    