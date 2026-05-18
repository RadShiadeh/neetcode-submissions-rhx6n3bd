class Solution:
    def __init__(self):
        pass
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self._backtrack(nums, [], 0)
        return self.res
    
    def _backtrack(self, nums, subset, idx):
        xorr = 0
        for n in subset:
            xorr ^= n
        
        self.res += xorr

        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self._backtrack(nums, subset, i+1)
            subset.pop()