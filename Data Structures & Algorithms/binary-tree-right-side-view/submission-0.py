# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res = self.dfs(root, res, 0)
        return res
    
    def dfs(self, node, res, depth):
        if not node:
            return
        
        if depth == len(res):
            res.append(node.val)
        
        self.dfs(node.right, res, depth+1)
        self.dfs(node.left, res, depth+1)

        return res