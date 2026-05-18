# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float("-inf")
        res = self._dfs(root, res)
        return res

    
    def _dfs(self, node, res):
        if not node:
            return res
        
        left = self._get_max(node.left)
        right = self._get_max(node.right)
        res = max(res, left + right + node.val)

        res = self._dfs(node.left, res)
        res = self._dfs(node.right, res)

        return res
    
    def _get_max(self, node):
        if not node:
            return 0
        
        left_max = self._get_max(node.left)
        right_max = self._get_max(node.right)
        
        path = node.val + max(left_max, right_max)
        return max(0, path)