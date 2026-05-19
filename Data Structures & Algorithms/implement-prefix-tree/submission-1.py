class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True

    def search(self, word: str) -> bool:
        if not word:
            return True
        
        node = self.root
        for w in word:
            node = node.children.get(w, None)
            if node and node.end:
                return True
            elif not node:
                return False
        
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        
        node = self.root
        for c in prefix:
            node = node.children.get(c, None)
            if not node:
                return False
        
        return True