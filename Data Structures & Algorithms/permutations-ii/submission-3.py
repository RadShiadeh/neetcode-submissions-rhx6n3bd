class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self._backtrack(nums, [], [False] * len(nums))
        return self.res
    
    def _backtrack(self, nums, subset, visited):
        if len(subset) == len(nums):
            self.res.append(subset.copy())
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            subset.append(nums[i])
            visited[i] = True
            self._backtrack(nums, subset, visited)

            visited[i] = False
            subset.pop()