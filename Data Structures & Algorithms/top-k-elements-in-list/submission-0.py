class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for n, f in freq.items():
            bucket[f].append(n)
        
        res = []
        for i in range(len(bucket) -1, -1, -1):
            if bucket[i]:
                for v in bucket[i]:
                    res.append(v)
                    if len(res) == k:
                        return res
        
        return res