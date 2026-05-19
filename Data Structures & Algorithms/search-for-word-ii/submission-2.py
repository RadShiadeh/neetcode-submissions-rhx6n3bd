class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or len(words) == 0:
            return []

        trie = TrieNode()
        for w in words:
            trie.insert(w)

        res = []
        seen = set()
        len_rows = len(board)
        len_cols = len(board[0])

        for i in range(len_rows):
            for j in range(len_cols):
               self._backtrack(board, trie, "", i, j, res, seen)

        return res

    def _backtrack(self, board, node, word, i, j, res, seen):
        if (
            (i < 0 or i >= len(board))
            or (j < 0 or j >= len(board[i]))
            or board[i][j] not in node.children
            or (i, j) in seen
        ):
            return
        
        c = board[i][j]
        seen.add((i, j))
        next_node = node.children[c]
        word += c
        if next_node.end:
            res.append(word)
            next_node.end = False
        
        self._backtrack(board, next_node, word, i, j-1, res, seen)
        self._backtrack(board, next_node, word, i, j+1, res, seen)
        self._backtrack(board, next_node, word, i-1, j, res, seen)
        self._backtrack(board, next_node, word, i+1, j, res, seen)

        seen.remove((i, j))

        return res, seen