def numEnclaves(grid):
    num=0
    vis=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num=num+grid[i][j]
            if grid[i][j]==1 and (i*j==0 or i==len(grid)-1 or j==len(grid)-1) :
                def dfs(grid, i, j, vis):
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or vis[i][j] or grid[i][j] == 0:
                        return 0
                    else:
                        vis[i][j] = True
                        return 1 + dfs(grid, i + 1, j, vis) + dfs(grid, i - 1, j, vis) + dfs(grid, i, j + 1, vis) + dfs(grid, i, j - 1, vis)
                #print(i,j,dfs(grid,i,j,vis))
                num=num-dfs(grid,i,j,vis)
                
    return num


grid=[[0,0,0,1,1,1,0,1,0,0],
      [1,1,0,0,0,1,0,1,1,1],
      [0,0,0,1,1,1,0,1,0,0],
      [0,1,1,0,0,0,1,0,1,0],
      [0,1,1,1,1,1,0,0,1,0],
      [0,0,1,0,1,1,1,1,0,1],
      [0,1,1,0,0,0,1,1,1,1],
      [0,0,1,0,0,1,0,1,0,1],
      [1,0,1,0,1,1,0,0,0,0],
      [0,0,0,0,1,1,0,0,0,1]]

grid=[[0,1,1,0,0]]
print(len(grid[0]))
print(numEnclaves(grid))