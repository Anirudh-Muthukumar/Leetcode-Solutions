import collections

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        if board==[]:
            return board
            
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        # Visit all the neighboring cells from Border 'O' cells
        for r in range(m):
            for c in (0, n-1):
                if not visited[r][c] and board[r][c]=='O':
                    dfs = collections.deque()
                    dfs.append((r,c))
                    while dfs:
                        x, y = dfs.pop()
                        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j]=='O':
                                dfs.append((i, j))
                                visited[i][j] = True
    
        for c in range(n):
            for r in (0, m-1):
                if not visited[r][c] and board[r][c]=='O':
                    dfs = collections.deque()
                    dfs.append((r,c))
                    while dfs:
                        x, y = dfs.pop()
                        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j]=='O':
                                dfs.append((i, j))
                                visited[i][j] = True
                        
        # Left out cells are definitely surrounded cells which we need to change
        for r in range(1, m-1):
            for c in range(1, n-1):
                if not visited[r][c] and board[r][c]=='O':
                    board[r][c] = 'X'
                    visited[r][c] = True
        
        