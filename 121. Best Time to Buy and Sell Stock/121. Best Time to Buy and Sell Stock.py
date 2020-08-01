class Solution:
    def maxProfit(self, A):
        if A==[]:
            return 0
        
        res = float('-inf')
        min_so_far = A[0]
        n = len(A)
        
        for i in range(n):
            res = max(res, A[i] - min_so_far)
            min_so_far = min(min_so_far, A[i])
        
        return res
        
        