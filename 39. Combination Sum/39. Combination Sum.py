class Solution:
    def permute(self, A):
        
        def BT(A, l, r):
            if l==r:
                res.append(A)
            else:
                for i in range(l, r+1):
                    A[l], A[i] = A[i], A[l]
                    BT(A[:], l+1, r)
                    A[l], A[i] = A[i], A[l]

        res = []
        BT(A[:], 0, len(A)-1)
        return res