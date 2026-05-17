# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        self._traverse(root, res)

        return res
    
    def _traverse(self, node, res):
        if not node:
            return
        
        self._traverse(node.left, res)
        res.append(node.val)
        self._traverse(node.right, res)