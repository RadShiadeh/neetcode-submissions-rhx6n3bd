class Solution:
    def __init__(self):
        pass
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self._backtrack(nums, target, [], 0)
        return self.res
    def _backtrack(self, nums, target, subset, idx):
        s = sum(subset)
        if s == target:
            self.res.append(subset[:])
            return
        elif s > target:
            return
        
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self._backtrack(nums, target, subset, i)
            subset.pop()
