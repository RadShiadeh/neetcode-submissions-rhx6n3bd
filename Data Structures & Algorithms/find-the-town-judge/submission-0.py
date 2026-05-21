class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = set()
        trusties = {}
        for t in trust:
            trusting.add(t[0])
            if t[1] not in trusties:
                trusties[t[1]] = set()
            
            trusties[t[1]].add(t[0])
        
        print(trusting)

        print(trusties)

        for i in range(1, n+1):
            if i not in trusting and i in trusties and len(trusties[i]) == n-1:
                return i
        
        return -1
