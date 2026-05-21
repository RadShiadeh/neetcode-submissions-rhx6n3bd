class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                return self._dfs(grid, i, j, visited, res)
        
        return res
    
    def _dfs(self, grid, i, j, visited, res):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 1
        
        if (i, j) in visited:
            return 0
        
        visited.add((i, j))
        return self._dfs(grid, i+1, j, visited, res)+self._dfs(grid, i-1, j, visited, res)+self._dfs(grid, i, j+1, visited, res)+self._dfs(grid, i, j-1, visited, res)
