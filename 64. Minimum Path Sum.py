def minPathSum(self, grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    T = [x[:] for x in grid[:]]
    
    for i in range(1, m):
        T[i][0] += T[i-1][0]
    
    for j in range(1, n):
        T[0][j] += T[0][j-1]
    
    
    for i in range(1, m):
        for j in range(1, n):
            T[i][j] += min(T[i-1][j], T[i][j-1])
    
    return T[-1][-1]