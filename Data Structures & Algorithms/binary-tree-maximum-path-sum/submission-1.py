# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self._dfs(root)
        return self.res
    
    def _dfs(self, node):
        if not node:
            return 0
        
        left = max(self._dfs(node.left), 0)
        right = max(self._dfs(node.right), 0)

        path = node.val + left + right
        self.res = max(self.res, path)

        return node.val + max(left, right, 0)