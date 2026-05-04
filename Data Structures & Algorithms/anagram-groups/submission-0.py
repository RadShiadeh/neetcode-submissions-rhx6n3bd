class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq: dict[tuple[int], list[str]] = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            key = tuple(key)
            if key not in freq.keys():
                freq[key] = []
            
            freq[key].append(s)
        
        return list(freq.values())