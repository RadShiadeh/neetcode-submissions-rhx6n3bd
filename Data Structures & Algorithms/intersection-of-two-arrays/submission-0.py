class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        seen = set()

        for n in nums1:
            seen.add(n)
        
        for n in nums2:
            if n in seen:
                res.add(n)
        
        return list(res)