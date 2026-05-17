# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        
        val_p = p.val
        val_q = q.val

        curr = root
        while curr:
            if curr.val < val_p and curr.val < val_q:
                curr = curr.right
            elif curr.val > val_p and curr.val > val_q:
                curr = curr.left
            else:
                return curr
        
        return root