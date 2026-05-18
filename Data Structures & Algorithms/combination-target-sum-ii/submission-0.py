class Solution:
    def __init__(self):
        pass
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self._backtrack(candidates, target, [], 0)
        return list(self.res)
    
    def _backtrack(self, candidates, target, subset, idx):
        s = sum(subset)
        if s == target:
            self.res.append(subset.copy())
            return
        elif s > target:
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            subset.append(candidates[i])
            self._backtrack(candidates, target, subset, i+1)
            subset.pop()