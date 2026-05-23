# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        res = -1
        _, res = self._inorder_traverse(root, k, res)
        return res
        
    def _inorder_traverse(self, node, k, res):
        if not node or k == 0:
            return k, res
        
        k, res = self._inorder_traverse(node.left, k, res)
        k-=1
        if k == 0:
            res = node.val
            return k, res
        k, res = self._inorder_traverse(node.right, k, res)

        return k, res