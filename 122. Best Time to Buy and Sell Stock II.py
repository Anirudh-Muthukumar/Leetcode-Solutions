class Solution:
    def maxProfit(self, A):
        profit = 0
        if len(A)>0:
            prev = A[0]
            for i in range(len(A)):
                if A[i]>prev:
                    profit += A[i]-prev
                prev = A[i]
        
        return profit