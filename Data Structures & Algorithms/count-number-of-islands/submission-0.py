class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    self._dfs(grid, i, j)
        
        return res
    
    def _dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        self._dfs(grid, i+1, j)
        self._dfs(grid, i-1, j)
        self._dfs(grid, i, j+1)
        self._dfs(grid, i, j-1)