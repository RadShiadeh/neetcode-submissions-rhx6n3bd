# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        self._traverse(root, res)
        return res
    
    def _traverse(self, root, res):
        if not root:
            return
        
        self._traverse(root.left, res)
        self._traverse(root.right, res)
        res.append(root.val)

        return