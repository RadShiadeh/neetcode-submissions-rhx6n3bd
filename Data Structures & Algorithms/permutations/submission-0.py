class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self._backtrack(nums, [], [False] * len(nums))
        return self.res
    
    def _backtrack(self, nums, subset, visited):
        if len(nums) == len(subset):
            self.res.append(subset.copy())
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            subset.append(nums[i])
            visited[i] = True
            self._backtrack(nums, subset, visited)

            subset.pop()
            visited[i] = False