class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i, j])
        
        time = 0
        
        while q:
            for _ in range(len(q)):
                x, y = q.pop(0)
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        grid[i][j]=2
                        fresh -= 1
                        q.append([i, j])
            time+=1
        
        if fresh==0:
            return max(0, time-1)
        
        return -1
                