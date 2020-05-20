class Solution:
    def floodFill(self, image, sr, sc, newColor):
        
        m = len(image)
        if m==0:
            return []
        
        n = len(image[0])
        
        oldColor = image[sr][sc]
        visited = set()
        
        def dfs(x, y):

            image[x][y] = newColor
            visited.add((x, y))
            
            if 0<=x+1<m and 0<=y<n and image[x+1][y]==oldColor and (x+1, y) not in visited:
                dfs(x+1, y)
            if 0<=x-1<m and 0<=y<n and image[x-1][y]==oldColor and (x-1, y) not in visited:
                dfs(x-1, y)
            if 0<=x<m and 0<=y+1<n and image[x][y+1]==oldColor and (x, y+1) not in visited:
                dfs(x, y+1)
            if 0<=x<m and 0<=y-1<n and image[x][y-1]==oldColor and (x, y-1) not in visited:
                dfs(x, y-1)
        
        dfs(sr, sc)
        
        return image
            
            
            
            