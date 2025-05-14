class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #1.把語邊邊相連變為0
        #2.if==1找相連病變為0
        #3.找最大
        m = len(grid)
        n = len(grid[0])
        def DFS(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == 1:
                grid[i][j] =0
                DFS(i-1,j)
                DFS(i+1,j)
                DFS(i,j-1)
                DFS(i,j+1)
                return
            
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0 or i==m-1 or j ==n-1:
                    DFS(i,j)
        
                     
        return sum([sum(x) for x in grid])