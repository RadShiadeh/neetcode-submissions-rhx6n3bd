class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _seen = set()

        for n in nums:
            if n in _seen:
                return True
            _seen.add(n)
        
        return False