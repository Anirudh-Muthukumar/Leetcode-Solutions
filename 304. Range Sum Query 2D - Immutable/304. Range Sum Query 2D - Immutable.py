class NumMatrix:

    def __init__(self, A):
        if len(A)==0:
            return 
        m, n = len(A), len(A[0])
        self.rangeSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.rangeSum[i][j] = self.rangeSum[i-1][j] + self.rangeSum[i][j-1] - self.rangeSum[i-1][j-1] + A[i-1][j-1]
            

    def sumRegion(self, p, q, r, s):
        p, q, r, s = p+1, q+1, r+1, s+1
        return self.rangeSum[r][s] - self.rangeSum[r][q-1] - self.rangeSum[p-1][s] + self.rangeSum[p-1][q-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)