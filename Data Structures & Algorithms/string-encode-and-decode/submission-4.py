class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            l = int(s[i:j])
            i = j + 1
            j = i + l
            w = s[i:j]
            decoded.append(w)
            i = j

        
        return decoded
            