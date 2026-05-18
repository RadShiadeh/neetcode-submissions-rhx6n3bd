# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        self._compute(root)
        return self.res
    
    def _compute(self, node):
        if not node:
            return
        
        left = self._get_height(node.left)
        right = self._get_height(node.right)
        self.res = max(self.res, left + right)

        self._compute(node.left)
        self._compute(node.right)
    
    def _get_height(self, node):
        if not node:
            return 0
        
        return 1 + max(self._get_height(node.left), self._get_height(node.right))