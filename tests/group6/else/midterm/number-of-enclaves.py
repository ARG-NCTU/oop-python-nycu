from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Return the number of land cells in the grid for which we cannot walk off the boundary of the grid in any number of moves.

        Parameters:
            grid (List[List[int]]): A binary matrix where 0 represents a sea cell and 1 represents a land cell.

        Returns:
            int: The number of land cells that cannot reach the boundary.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> grid1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
            >>> solution.numEnclaves(grid1)
            3

            # Example 2:
            >>> grid2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
            >>> solution.numEnclaves(grid2)
            0
        """
        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j):
            nonlocal grid, m, n, dirs
            if grid[i][j] == 0:
                return 
            
            grid[i][j] = 0
            for di, dj in dirs:
                0 <= i+di < m and 0 <= j+dj < n and dfs(i + di, j + dj)

            # if i - 1 >= 0:
            #     dfs(i - 1, j)
            # if i + 1 < m:
            #     dfs(i + 1, j) 
            # if j - 1 >= 0:
            #     dfs(i, j - 1)
            # if j + 1 < n:
            #     dfs(i, j + 1) 

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
            
        return sum([sum(x) for x in grid])
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    