class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self._dfs(board, word, visited, 0, i, j):
                    return True
        
        return False
    

    def _dfs(self, board, word, visited, idx, i, j):
        if len(word) == idx:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if visited[i][j] or board[i][j] != word[idx]:
            return False

        visited[i][j] = True
        found = (
            (self._dfs(board, word, visited, idx+1, i+1, j)) or
            (self._dfs(board, word, visited, idx+1, i-1, j)) or
            (self._dfs(board, word, visited, idx+1, i, j+1)) or
            (self._dfs(board, word, visited, idx+1, i, j-1))
        )
        visited[i][j] = False
        return found
