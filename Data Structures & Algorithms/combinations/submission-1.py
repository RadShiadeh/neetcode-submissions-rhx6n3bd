class Solution:
    def __init__(self):
        pass
    def combine(self, n: int, k: int) -> List[List[int]]:        
        self.res = []
        self._backtrack(n, k, [], 1)
        return self.res
    
    def _backtrack(self, n, k, subset, idx):
        if len(subset) == k:
            self.res.append(subset.copy())
            return
        
        for i in range(idx, n+1):
            subset.append(i)
            self._backtrack(n, k, subset, i+1)
            subset.pop()