class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self._backtrack(nums, [], 0)
        return self. res
    
    def _backtrack(self, nums, subset, idx):
        self.res.append(subset.copy())
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self._backtrack(nums, subset, i+1)
            subset.pop()