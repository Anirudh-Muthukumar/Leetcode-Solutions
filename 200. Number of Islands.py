
def numIslands(grid):
    if grid==[]:
        return 0
    
    m, n = len(grid), len(grid[0])
    islands = 0
    visited = set()
    
    def dfs(x, y):
        visited.add((x, y))
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0<=i<m and 0<=j<n and (i, j) not in visited and grid[i][j]=="1":
                dfs(i, j)
    
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and grid[i][j]=="1":
                dfs(i, j)
                islands += 1
    
    return islands