class Solution:
    def islandPerimeter(self, grid):
        if grid==[]:
            return 0
        
        dfs = {}
        m, n = len(grid), len(grid[0])
        perimeter = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    q = [(r, c)]
                    
                    while q:
                        (x, y) = q.pop()  
                        if visited[x][y]:
                            continue
                        visited[x][y] = True
                        
                        
                        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0<=i<m and 0<=j<n and visited[i][j]==False and grid[i][j]==1:
                                q.append((i, j))
                            elif not 0<=i<m or not 0<=j<n or grid[i][j]==0:
                                perimeter += 1 
                        
                    return perimeter
        
        return perimeter
                                
        
        
        