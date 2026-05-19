class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):        
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w] 
            node.count += 1
    
    def prefix_count(self, pref):
        node = self.root
        for c in pref:
            node = node.children.get(c, None)
            if not node:
                return 0
        
        return node.count


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.prefix_count(pref)