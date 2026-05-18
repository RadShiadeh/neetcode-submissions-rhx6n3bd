class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        self._backtrack(nums, [], [False] * len(nums))
        return list(self.res)
    
    def _backtrack(self, nums, subset, visited):
        if len(subset) == len(nums):
            self.res.add(tuple(subset.copy()))
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            subset.append(nums[i])
            visited[i] = True
            self._backtrack(nums, subset, visited)

            visited[i] = False
            subset.pop()