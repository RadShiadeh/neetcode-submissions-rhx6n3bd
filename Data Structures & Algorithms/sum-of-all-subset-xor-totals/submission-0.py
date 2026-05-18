class Solution:
    def __init__(self):
        pass
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self._backtrack(nums, [], 0)
        return self.res
    
    def _backtrack(self, nums, subset, idx):
        if idx == len(nums):
            xorr = 0
            for n in subset:
                xorr ^= n
            self.res += xorr
            return

        subset.append(nums[idx])
        self._backtrack(nums, subset, idx+1)
        subset.pop()
        self._backtrack(nums, subset, idx+1)