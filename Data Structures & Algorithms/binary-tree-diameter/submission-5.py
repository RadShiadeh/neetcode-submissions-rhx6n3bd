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
        
        _, res = self._compute(root)

        return res
    
    def _compute(self, node):
        if not node:
            return 0, 0
        
        lh, ld = self._compute(node.left)
        rh, rd = self._compute(node.right)

        height = 1 + max(lh, rh)
        res = max(ld, rd, lh + rh)

        return height, res