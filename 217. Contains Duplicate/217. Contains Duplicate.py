class Solution:
    def containsDuplicate(self, A):
        T = set()
        for i in range(len(A)):
            if A[i] not in T:
                T.add(A[i])
            else:
                return True
        
        return False