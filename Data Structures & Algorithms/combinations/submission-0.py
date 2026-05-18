class Solution:
    def __init__(self):
        pass
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        
        self.res = []
        self._backtrack(nums, k, [], 0)
        return self.res
    
    def _backtrack(self, nums, k, subset, idx):
        if len(subset) == k:
            self.res.append(subset.copy())
            return
        elif len(subset) > k:
            return
        
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self._backtrack(nums, k, subset, i+1)
            subset.pop()