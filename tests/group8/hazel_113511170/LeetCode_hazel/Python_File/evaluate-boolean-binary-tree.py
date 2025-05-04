# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def aux(self,root):
        if root==None:
            return None
        if root.val==0:
            return False
        if root.val==1:
            return True
        if root.val==2:
            return self.aux(root.left) or self.aux(root.right)
        elif root.val==3:
            return self.aux(root.left) and self.aux(root.right)
        
    def evaluateTree(self, root) :
        return self.aux(root)

