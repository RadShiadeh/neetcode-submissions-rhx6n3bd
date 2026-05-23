# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._bfs(root)
    

    def _recursive(self, node):
        if not node:
            return 0
        
        return 1 + max(self._recursive(node.left), self._recursive(node.right))
    
    def _bfs(self, node):
        if not node:
            return 0
        
        depth = 0
        queue = deque([node])
        while queue:
            for i in range(len(queue)):
                n = queue.popleft()
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            depth += 1
        
        return depth