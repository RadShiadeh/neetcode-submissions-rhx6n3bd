# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, val):
            if not node:
                return 0
            
            res = 1 if node.val >= val else 0
            val = max(val, node.val)
            res += dfs(node.right, val)
            res += dfs(node.left, val)
            return res
        res = dfs(root, float("-inf"))
        return res