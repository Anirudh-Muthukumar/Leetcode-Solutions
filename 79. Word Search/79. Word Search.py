class Solution:
    def exist(self, A, word):
        
        m, n = len(A), len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(x, y, word):
            if word == '':
                return True
            
            visited[x][y] = True
            
            for i, j in ((x+1, y), (x-1, y), (x,y+1), (x,y-1)):
                if 0<=i<m and 0<=j<n and not visited[i][j] and A[i][j]==word[0]:
                    if dfs(i, j, word[1:]):
                        return True
            
            # backtrack
            visited[x][y] = False
            return False
                    
        
        for i in range(m):
            for j in range(n):
                if A[i][j]==word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        
        return False