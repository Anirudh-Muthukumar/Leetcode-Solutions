class Solution:
    def minFallingPathSum(self, A):
        m, n = len(A), len(A[0])
        
        for i in range(1, m):
            for j in range(n):
                top = A[i-1][j]
                top_left = float('inf')
                top_right = float('inf')
                if j>0:
                    top_left = A[i-1][j-1]
                if j<n-1:
                    top_right = A[i-1][j+1]
                    
                A[i][j] += min(top, top_left, top_right)
        
            
        return min(A[m-1])
                