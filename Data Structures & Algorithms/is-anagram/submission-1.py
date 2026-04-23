class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_chars = {}
        s_chars = {}

        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            
            t_chars[ct] = t_chars.get(ct, 0) + 1
            s_chars[cs] = s_chars.get(cs, 0) + 1
        
        for c, f in s_chars.items():
            if t_chars.get(c, 0) != s_chars[c]:
                return False
        
        return True