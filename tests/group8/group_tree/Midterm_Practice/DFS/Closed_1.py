class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j):
            nonlocal grid, m, n, dirs
            if grid[i][j] == 0:
                return 
            
            grid[i][j] = 0
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n:
                    dfs(i+di, j+dj)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(1,n-1):
            dfs(0, j)
            dfs(m-1, j)
            
        return sum([sum(x) for x in grid])